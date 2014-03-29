# manifestly blog

1.  Make changes on the middleman branch, commit, push:

        git checkout middleman
        # change content
        git add
        git commit
        git put

2.  Build the changes:

        bundle exec middleman build

3.  At this point, `git status` won't show any changes since all the content is ignored in the middleman branch.

4.  Switch to master:

        git checkout master
        
5.  Run the update script:

        python update.py

6.  Check the status:

        git status
        
7.  Add everything, commit, and push:

        git add --all
        git commit
        git put
