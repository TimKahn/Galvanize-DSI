from math import pi
import pandas as pd
#interactive image modules
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
#dendogram modules
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist


from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LinearColorMapper,
    BasicTicker,
    PrintfTickFormatter,
    ColorBar,
)
from bokeh.plotting import figure
from flask import Flask, render_template, request
import webbrowser, threading, os

app = Flask(__name__)  
    
def get_dataframe_and_axes(fname=None, fname2=None, gene_col_name=None, max_value = None):
    ''' arbitrary data for now '''
    #count file
    df_c = pd.read_csv(fname)
    #p_value file
    df_p = pd.read_csv(fname2)
    len_p_val = len(list(df_p)) 
    len_c_val = len(list(df_c))
    # renames the A1 position to gene_col_name if not found. not very smart. 
    if list(df_c)[0] != gene_col_name:
        df_c.rename(columns = {list(df_c)[0]: gene_col_name}, inplace = True)
    if list(df_p)[0] != gene_col_name:
        df_p.rename(columns = {list(df_p)[0]: gene_col_name}, inplace = True)
    #drop rows with values greater than max p_value
    # list(df_p)[-1] is the p_value adjusted based off our r script. 
    df_p = df_p[df_p[list(df_p)[-1]] <= max_value]  
    
    
    while df_p.shape[0] > max_num:
        max_value -= .01
        if max_value == 0:
            print(' p = 0, something wrong with data')
            quit()
                        
        df_p = df_p[df_p[list(df_p)[-1]] <= max_value]   
        print('auto adjusted p-value cutoff to keep below maximum points')
        print('new cutoff is: ' + str(max_value))
    
    
    #merge on p_value dataframe
    df_c = pd.merge(df_c, df_p, 
                    on='Gene ID')    
    
    #keep only columsn from original count dataframe
    df_c = df_c[df_c.columns[:len_c_val]]
    df_c['Gene_ID'] = df_c[gene_col_name].astype(str)
    df_c.drop([gene_col_name], axis=1, inplace=True)
    df_c = df_c.set_index('Gene_ID')
    
    df_p['Gene_ID'] = df_p[gene_col_name].astype(str)
    df_p.drop([gene_col_name], axis=1, inplace=True)
    df_p = df_p.set_index('Gene_ID')
    
    
    df_c.columns.name = 'Samples' 
    gene_lst = list(df_c.index)
    sample_lst = list(df_c.columns)
    df_c = pd.DataFrame(df_c.stack(), columns=['counts']).reset_index()
    df_p =df_p.reset_index()
    # only need the id and the p_adj for now. 
    #df_p= df_p[df_p.columns[[0,-1]]]
        
    return df_c, sample_lst, gene_lst, df_p
    
def make_heatmap_object(df, sample_lst, gene_lst, df_p):
    ''' makes a bokeh figure '''
    colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
    colors2 =['#E5B000', '#CE9514', '#B77F24', '#A06C30','#895D36', '#724F39', '#5B4236', '#443430', '#2D2624','#161414', '#000000']
    colors = colors2[::-1]
    
    mapper = LinearColorMapper(palette=colors, low=df['counts'].min(), high=df['counts'].max())

    df = pd.merge(df, df_p, on = 'Gene_ID')    
    source = ColumnDataSource(df)
    
    TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"

    # p is a bokeh figure object 
    p = figure(title="Gene Expression",
               x_range=sample_lst, y_range=gene_lst,
               x_axis_location="above", plot_width=600, plot_height=900,
               tools=TOOLS, toolbar_location='below')
    
    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "5pt"
    p.axis.major_label_standoff = 0
    p.xaxis.major_label_orientation = pi / 3

    p.rect(x="Samples", y="Gene_ID", width=1, height=1,
           source=source,
           fill_color={'field': 'counts', 'transform': mapper},
           line_color=None)

    color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size="5pt",
                         ticker=BasicTicker(desired_num_ticks=len(colors)),
                         formatter=PrintfTickFormatter(format="%d"),
                         label_standoff=6, border_line_color=None, location=(0, 0))
    p.add_layout(color_bar, 'right')

    p.select_one(HoverTool).tooltips = [
         ('[Sample, Gene_ID]', '@Samples @Gene_ID'),
         ('Transformed Count', '@counts'),
         ('P-Adj', '@padj'),
    ]
    return p

def data_names(directory, type):
    return  [file for file in os.listdir(directory) if file.endswith(type)]
    
def image_names(directory):
    return  [file for file in os.listdir(directory)]
    
@app.route('/input')
def results():     
    file_arr = data_names(data_path, data_type) 
    return render_template( 'input.html', count_file = file_arr, 
                            p_file = file_arr, plot_type = avail_figure, 
                            p_value = p_possible)

@app.route("/visualize", methods=['POST'])
def visualize():   
    graph = request.form['graph_type']
    highest_p = float(request.form['p_return'])
    img_arr = image_names(image_path)
    #only special graph
    
    if graph == avail_figure[-1]:
        df, sample_lst, gene_lst, df2 = get_dataframe_and_axes( os.path.join('data',request.form['file_1']),     
                                                                os.path.join('data',request.form['file_2']), 'Gene ID', 
                                                                highest_p)
        heatmap = make_heatmap_object(  df, sample_lst, 
                                        gene_lst,df2)
    else:
        print('Unable to plot Volcano')    
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    # note that heapmap below is defined under if-name-main block
    script, div = components(heatmap)
    
    html = render_template(
        'visualize.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
        img_list = img_arr,
        img_path = image_path
        )
    return encode_utf8(html)    

# maybe make a landing page with redirect to data enter page.  

@app.route('/')
def home():
    return render_template('home.html')
   
# about page
@app.route('/about')
def about():
    return render_template('about.html')

# contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')  
    
if __name__ == '__main__':
    #configs
    avail_figure = [ 'Volcano','Heatmap']
    data_path ='data'
    data_type = '.csv'
    image_path = 'static/fig'
    max_num = 200
    p_possible = [.05, .04, .03, .02, .01]          
    # threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
    app.run('0.0.0.0', port=8000)
