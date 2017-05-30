# Flask afternoon goal
The end goal of this afternoon is to have a Flask app using a Bootstrap template deployed on an Amazon AWS EC2 free tier.

So we'll proceed in two parts:
* Part 1: getting a Flask app using a desired Bootstrap template running locally.
* Part 2: getting that app deployed and running on an EC2 instance.

## Part 1  

### Bootstrap

We use CSS to style html pages. With CSS we can control colors, fonts, spacing and anything else about the appearance.

Instead of working with CSS directly we can use [Bootstrap](http://getbootstrap.com/), which has standard templates.

#### Installation
We'll be downloading code associated with their [examples](http://getbootstrap.com/getting-started/#examples).  Click on this examples link and once on the page click on the _downloading the Bootstrap repository_ link in blue text, as shown below.
![image](images/img_bootstrap_repo_link.png)

It should be about 5 MB zipped archive that uncompresses to about 11 MB into a directory called `Bootstrap-3.3.7`. It's going to contain the files needed to recreate and then customize our own web page.

#### Starter example
Bootstrap has a bunch of examples built already. It's standard to start with those and modify them for your needs.

Take a look at their [examples](http://getbootstrap.com/getting-started/#examples) again.

We'll start with the simplest one, the [starter template](http://getbootstrap.com/examples/starter-template/).

We're going to want to have the following file structure in a folder called something like `web_app`:

web_app  
* app.py (this is our flask app)  
* templates/ (contains .html files)  
* static/  
  * css/ (contains .css files)  
  * fonts/  (contains fonts)  
  * js/  (contains .js files)

1. Go to `Bootstrap-3.3.7/dist/` and copy the `css`, `fonts`, and `js` folders.  Paste them into your `static` folder. 

1. In `Bootstrap-3.3.7/docs/examples/starter-template` find the `index.html` file and put that in the `templates` folder.  Then drag the `starter-template.css` file into the `static/css` folder.

1. Now, if you open the `index.html` file in your `templates` folder you should see a region where several files are linked:
![image](images/index_before_renaming.png)

You need to a) find these files in `Bootstrap-3.3.7` and then b) paste them into the following locations in your `static` folder:
![image](images/index_after_renaming.png)

You aren't quite done.  There are some links at the bottom of the `index.html` that need to be updated too:
![image](images/bottom_index_before_renaming.png)

And these links should look like this when you are done:
![image](images/bottom_index_after_renaming.png)

Now see if you can run your app locally.
`$ python app.py`

## Part 2  

1. Get your `web_app` folder up on your Github page. We will be cloning it to our EC2 instance.

1. Log into the AWS Console and Launch an EC2 instance.
![image](images/001_Launch_EC2.png)

1. Create an instance.
![image](images/002_Create_an_Instance.png)

1. Go to community AMI to select a machine image.
![image](images/003_Community_AMI_select_image.png)

1. Select Erich's DSI template image.
![image](images/004_Select_DSI_image.png)

1. Choose the free tier instance.
![image](images/005_Choose_Instance_free_tier.png)

1. Click configure instance details.
![image](images/006_Click_Configure_Instance_Details.png)

1. Click add storage.
![image](images/007_Click_Add_Storage.png)

1. Click add tags.
![image](images/008_Click_Add_tags.png)

1. Give your tag a name (for instance *my_web_app*).
![image](images/009_Give_your_tag_a_name_my_web_app.png)

1. Configure your security group by adding a rule.
![image](images/010_Configure_security_group_add_rule.png)

1. Edit inbound rules and select port (using 8105, could use other).
![image](images/011_Edit_inbound_rules_and_set_port.png)

1. Review and launch.
![image](images/012_Review_and_launch.png)

1. Launch.
![image](images/013_Launch.png)

1. Select or make key-pair and download.
![image](images/014_Select_or_make_key_pair_and_download.png)

1. Launch the instance.
![image](images/015_Launch_the_instance.png)

1. Verify that the instance is launched.
![image](images/016_Verify_that_instance_is_launched.png)

1. Put the key-pair in your local .ssh folder and chmod.
![image](images/017_put_key_pair_in_ssh_and_chmod.png)

1. Make a config file in .ssh folder
![image](images/018_make_config_in_ssh.png)

1. Get details of your instance to add to config file.
![image](images/019_click_on_launch_details.png)

1. Get the IPv4 address from the bottom right.
![image](images/020_get_IPv4_address_from_instance_bottom_right.png)

1. Fill in details in the config file and give the Hostname.
![image](images/021_fill_in_details_in_config_file_and_give_host_name.png)

1. Now we can finally ssh into our web_app.
![image](images/022_ssh_into_web_app.png)

1. Continue connecting.
![image](images/023_continue_connecting.png)

1. Check for updates.
![image](images/024_check_for_updates.png)

1. Check that you are logged into an ubuntu server.
![image](images/025_should_be_logged_into_ubuntu_server.png)

1. Clone your web app on Github.
![image](images/026_clone_your_web_app_repo.png)

1. Clone it into your EC2 instance.
![image](images/027_clone_your_web_app_repo_onto_server.png)

1. Start a `tmux` session.
![image](images/028_get_into_tmux.png)

1. Modify your flask app's port to be consistent with the port you specified in your instance, and add threading.
![image](images/029_modify_flask_app_port_threading.png)

1. Now run your app in the tmux session.
![image](images/030_run_python_app_in_tmux.png)

1. Detach (but leave running) your tmux session by hitting Ctrl-b d.
![image](images/031_detach_from_tmux_session_ctrlbd.png)

1. Our site, finally, should be deployed!
![image](images/032_go_to_deployed_site.png)

Not hard, right?

Now you can customize by adding and altering html templates in the templates folder.  See the Cooper Corn app.





