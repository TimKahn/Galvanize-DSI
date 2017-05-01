## Learn-git Notes

Git is version-control software that lets you keep track of changes to a project
over time.  Git records and stores changes you make to a project and let's you
access these changes when needed.

Git projects have three parts:
* A working directory (or repository, folder) where you'll be making, changing,
and deleting files.
* A staging area where you'll add new/modified files to the project.
* A .git repository that stores the changes to the files through a series of
sequential commits.

These notes will try to walk you through step-by-step git use and syntax.


### Configuration
From the command line, configure the user name and email.
Assume the username is **Pat_Smith** with email **pat.smith@aol.com**.
Generally these match the Github username and email account.

```bash
$ git config --global user.name "Pat_Smith"  
$ git config --global user.email "pat.smith@aol.com"  
```

### Make a git repository (one way to do it)  
For this part we'll use the arbitrarily name repository `project_dir`.  

```bash
$ mkdir project_dir
$ cd project_dir
$ git init
```

With the the `git init` command we are telling git to make this repository (aka
directory) a git repository where all changes are tracked.  If you run the following
command you'll see what the `git init` command created.

```bash
$ ls -a
```

You should see a `.git` directory which will keep track of all changes in the
`project_dir` repository.

### Add and track a file
It turns out that Pat likes writing haiku.  Type the commands below - but first
make sure that you are in the `project_dir`.

```bash
$ nano haiku_1.txt
```

In the Nano text editor:

_Beauty, elegance,  
a flawless form of logic,  
my program is done._  

Type CTRL-O to write the file and CTRL-X to exit.  

With the addition of this new file see what the status of our git repo is:  
```bash
$ git status
```

`haiku_1.txt` should show up as _Untracked_.  This means that git is not tracking
changes to this file.  But let's decide to track it:

```bash
$ git add haiku_1.txt
```

This command adds the `haiku_1.txt` file to the _staging area_.  Let's check the 
status again.

```bash
$ git status
```

You should see that the `haiku_1.txt` file now appears under a "Change to be
committed."  It's in the _Staging Area_.  Note that you can remove it from
the staging area using:
```bash
$ git reset HEAD haiku_1.txt
```

Though it's in the staging area, it's still not tracked because it hasn't been
committed for the first time.  So let's `commit` the file that's in the staging
area.

```bash
$ git commit -m "Add initial version"
```

The -m followed by the text string is the commit message.  It's important to
provide brief messages describing what you did.  

If you just typed `$ git commit` and forgot the -m and message you'll be directed
to VI to enter the message.  **Don't panic.**  Just type 'i' to _insert_ text, then
type your text, then hit `Esc` to get out of the VI insert mode and back into normal
mode, then type ':' to enter the command line mode, then after the colon type
`:wq` to write the file and then quit.  See?  Easy.

Now that the file is committed let's check the status again.

```bash
$ git status
```

You should see that you are on the master branch and there's nothing to commit.
But Pat didn't actually write that poem - a citation needs to be added.  So open
up `haiku_1.txt` with your favorite text editor and add the citation:

_Beauty, elegance,  
a flawless form of logic,  
my program is done._

_https://www.ncwit.org/blog/you-can-code-can-you-knit_

Now save the file and check it's status.  You should see that the file is modified.
Add and commit it.

```bash
$ git add haiku_1.txt
$ git commit -m "Add citation"
```

### See commits and revert to an earlier version of a file

At this point we've committed `haiku_1.txt` twice.  Let's see the log of these
commits.

```bash
$ git log
```

You should see two commits.  Each will start with a commit identifier that you can use
to access that commit, followed by the author, date, and commit message.

If you want to see just the commit you are working on instead of the entire log:
```bash
$ git show HEAD
```

You've noticed that Pat screwed up the citation.  It should be:
_https://www.ncwit.org/blog/you-can-code-can-you-haiku_

At this point Pat could 1) edit the file again, change the citation, add it
and commit it, or 2) just reset to the initial commit, and then add the citation
to the original file, and then add it and commit it.  1) is the way to go, but
for teaching purposes (to show you how to revert a file) let's do 2).

```bash
$ git reset --hard 34329abb9e4384f1f8dc9e1a1a770891c95aaf38
```

Note the commit identifier (the _SHA_, the Secure Hash Algorithm) associated with
Pat's initial commit.  Here the entire SHA is pasted, but you need only the first
seven characters.  Without the `--hard` specification the project HEAD is reset to
the indicated commit, but the files are still in their present form (which has
been modified since that commit).

Now you can edit the file with your text editor, add it and commit it.

## Branching
Usually in git you work on the _master_ branch, but you can create branches of a
project to explore different versions of a project.  If a version in one of the 
branches works out, you can then merge it back into the master branch.  

To check which branch you are presently on:
```bash
$ git branch
```
The branch you are on will have and asterisk on it (\*).  

To make a new branch:
```bash
$ git branch name_of_new_branch
```
To switch to the new branch:
```bash
$ git checkout branch_name
```
You can (and should!) add/modify/delete and commit files on this new branch just
like you would the master.

### Merging
Eventually you may want to merge the work you've done on a branch into the
master branch.

First switch to the master branch:
```bash
$ git checkout master
```
Then merge your branch (branch1) into it:
```bash
$ git merge branch1
```

#### Merge conflicts
If some common parts of a file are different in two branches and you try to
merge them you'll get a merge conflict.  More specifically, you've made commits
in two different branches that alter the same line of a file in different ways.

A merge conflict will occur when you try a `git merge branch1` and it will indicate
in the file where the merge conflict occurs:

```bash
<<<<<<< HEAD
master version of line
=======
branch1 version of line
>>>>>>> branch1
```

To solve the merge conflict, between the arrows (<<<  >>>) pick which code you want
to keep and delete the rest.  Delete git's additions, too (HEAD === branch1 <<< >>>)
etc. Save the file.

Finally (assuming the conflicted file was file1.txt):
```bash
$ git add file1.txt
$ git commit -m "Resolve merge conflict"
```

Usually you delete branches when you are done with them.
```bash
$ git branch -d branch_name
```

## Git teamwork
On Git, you can work with someone else using something called a _remote_.  A
remote is a shared Git repository that allows multiple collaborators to work
on the same Git project from different locations.  Collaborators work on the 
project independently and merge changes together when they are ready.

In the DSI we use Github as a shared repository for the DSI course materials.
Each student has their own Github account, where they will most often first
_fork_ the daily DSI repo to their own Github account, and then _clone_ that
_remote_ locally.  Therefore the remote location that occurs in most of the 
directions below will most likely occur to the forked repo on each student's
Github account.

In order to get your own local (on your laptop) copy of a remote directory:
```bash
$ git clone remote_location your_name_for_the_cloned_repo
```

Let's say DSI student Pat Smith wants to clone the DSI Week 1, Day 1 repository
*Python Intro*.

The steps would be:
1) On Github, navigate to the https://github.com/zipfian/python-intro page.
2) _Fork_ the repo to Pat Smith's Github account.  Now Pat has his own copy.
3) Pat can now clone the directory on to his laptop:
```bash
$ git clone https://github.com/Pat_Smith/python-intro.git
```
Pat now has a local copy of the repo on his laptop.  Note that Pat didn't provide
a new name for the repo.  That's fine.  It will just keep the name python-intro.git.

The remote for the local copy of the repo is called _origin_.  When you are in a Git
repository you can see the location of the _origin_ by typing:
```base
$ git remote -v
```

Now let's say you were using a Github directory as a shared remote to collaborate
with someone.  The workflow would generally be:
1) Fetch and merge changes from the remote ( a `git pull` will do both)
2) Create a branch to work on a new feature
3) Develop the feature on your branch and commit your work
4) Do another `git pull` to update your work with any changes that occurred
while you were doing your work.
5) `git push` your branch up to the remote for review.

The syntax for the last command is
```bash
$ git push origin the_branch_you_want_to_push
```

If you are collaborating with someone, the branch name should *NOT* be master.
The idea is that the project owner will merge all the other branches into the
master branch after review.  However, if you are just working on your own files
and want to back it up on Github, then most likely you'll do this:
```bash
$ git push origin master
```
