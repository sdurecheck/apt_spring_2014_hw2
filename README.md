# APT Spring 2015: Assignment 2

## Assignment:

We will be working on simple web project. It is deployed and available on <https://immense-river-1564.herokuapp.com/>

### Setup:

 * Create GitHub account with SDU domain email.
 * Save ssh key to GitHub <https://github.com/settings/ssh>:
   - if you do not have `~/.ssh/id_rsa.pub` file, generate ssh key using ssh-keygen
   - `cat ~/.ssh/id_rsa.pub`
 * Fork the https://github.com/giAtSDU/apt_spring_2014_hw2 repository
 * Install Bottle: `sudo apt-get install python-bottle`

### Tasks:
 * Clone your forked repository to your local machine
 * Run the server: python server.py
 * Make sure that it works: goto <http://localhost:5000>; It should say `HW2 for APT Spring 2015`
 * Add a file to the participants directory, the filename must be in Name_Surname format. Write there information about your OS. (Use `lsb_release -a` command on linux)
 * Use git add to add that file to the repository.
 * Use git commit to commit your change. Use a meaningful message like "Added information YOUR NAME machine."
 * Use git push to send your change to your forked repository.
 * Look online to see if your change has been pushed.
 * Change `server.py` to make your name listed in the index page.
 * Run server and make sure your name is in the participants list <http://localhost:5000>: `python server.py`
 * Edit this README.md file, add your name under contributors list. Then add the file, commit it, and push it.
 * Add original repository as a remote `git remote add the_origin https://github.com/giAtSDU/apt_spring_2014_hw2.git`
 * Fetch changes from original repository using `git fetch the_origin`
 * Merge your changes with `the_origin/conflict` branch, resolve conflict, commit results
 * Make sure that application works: `python server.py`
 * Push your changes to your forked repository
 * Create a merge request on GitHub to the `spring2015` branch on original repository (https://github.com/giAtSDU/apt_spring_2014_hw2/pulls)

### For those who wants more:
 * This [application](https://immense-river-1564.herokuapp.com/) is deployed on heroku, you can do it too
 * Create an account on heroku.com
 * See the tutorial <https://devcenter.heroku.com/articles/getting-started-with-python-o>
 * Download the heroku toolbelt
 * Create heroku application using `heroku create`. Run it inside the project folder. Heroku toolbelt will crate a remote in your git project. See `git remote -v`
 * Deploy the project using `git push heroku master` 
 * Open an url that heroku generated for you

## Contributors:

 * 20 Robert Pattinson
 * 19 Kesha
 * 18 Megan Fox
 * 17 Nicki Minaj
 * 16 Beyonce
 * 15 Taylor Swift
 * 14 Selena Gomez
 * 13 Ronaldo
 * 12 Lil Wayne
 * 11 Kim Kardashian
 * German Ilyin
 * Roman Khabirov
 * 10 Drake
 * 9 Katy Perry
 * 8 Obama
 * 7 Michael Jackson
 * 6 Rihanna
 * 5 Shakira
 * 4 Eminem
 * 3 Miley Cyrus
 * 2 Lady Gaga
 * 1 Justin Bieber

## Git commands you might need

 * git help
 * git clone REPO
 * git add FILE
 * git status
 * git commit
 * git commit -m "MESSAGE"
 * git log | less
 * git push
 * git pull
 * git merge
 * git rebase

## Troubleshooting

 * https://stackoverflow.com/questions/4565700/specify-private-ssh-key-to-use-when-executing-shell-command-with-or-without-ruby
 * https://superuser.com/questions/232373/how-to-tell-git-which-private-key-to-use