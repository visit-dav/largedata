## Options for uploading large files

If a user needs to get data to VisIt developers for any reason,
the options available depend on the size of the files. In all of
the scenarios below, compression can help mitgate size limits.
If you have easy access to [7zip](7zip.md) compression tools, it
can often yield the best compression by sometimes a factor of 2-3x.

* Email
  * Works ok for small files, less than 5-10MB. The actual size limit
    depends on several factors which are likely outside the knowledge 
    of sender and recipeint.
* Attachments in our [SRE issues repo](https://github.com/visit-dav/live-customer-response/issues)
  * Only a handful of specific file extensions are supported.
  * Image files (`.gif`., `.png`, `.jpeg` and `.jpg`) < 10MB.
  * Raw text files (`.txt`, and `.log`) < 25MB.
  * Document files (`.pdf`, `.docx`, `.pptx`, and `.xlsx`) < 25MB.
  * Compressed files (`.gz`, `.zip`) < 25MB.
  * Because GitHub currently keys off *only* the file's extension, you can
    attach *any* format by simply faking and adding the `.gz` extension.
    To avoid confusion with a *real* gzip compressed file, also add an
    obvious intermediate extension such as `foo_data.7z.fake.gz`.
* [LLNL Anonymous FTP server](ftp://ftp.llnl.gov/incoming)
  * Works only to get data to VisIt developers with LLNL accounts.
  * Size limit depends on aggregate usage by all uploads there but probably < 1GB.
  * On Windows and linux, open a browser to the above link and drag and drop
    your files there. On OSX, from Finder select `Go->Connect to server` and enter
    `ftp://ftp.llnl.gov/incoming` and then drag and drop your files there.
  * Email VisIt developers with the name(s) of the files you uploaded there
    so they know to go get them.
  * Files uploaded there are readable only from LLNL firewalled networks and are
    purged regularly.
* Submit a PR from a [fork of this repository](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
  * Works for *any* VisIt developer
  * [Size limit is < 2GB](https://help.github.com/en/github/managing-large-files/about-git-large-file-storage)
  * See below for detailed instructions.

### Sending data via a Pull Request

This involves using a combination of a web browser on GitHub and
a shell command-line.

1. First, fork the repository on GitHub
   * Open a browser to [https://github.com/visit-dav/largedata](https://github.com/visit-dav/largedata)
   * Find and press the `Fork` button in the upper right
   * GitHub will ask you *where* you want to create the fork.
   * Create the fork in your personal space on GitHub.
   * Lets assume your GitHub name is `fizbo`.
   * Once you create the fork, clone it 
2. Create a local clone
   * Its best to use `ssh` to create the clone.
```
git clone git@github.com:fizbo/largedata.git
```
   * If you use `https`, be aware of [extra steps if you use two-factor authentication](https://help.github.com/en/github/authenticating-to-github/accessing-github-using-two-factor-authentication#using-two-factor-authentication-with-the-command-line)
```
git clone https://github.com/fizbo/largedata.git 
```
3. Add, commit and push file(s) to the `bindata` directory
   ```
   cd largedata/bindata
   git branch -b add-data-from-fizbo
   git add foo_data.tar.gz
   git commit -a -m 'adding my data file for upload'
   git push
   ```
   * **Note:** depending on the size of your files, it may take a 
   long time for the `git push` operation to complete.
   * Even after completing the steps above, the files are on GitHub but
   not accessible by anyone other than you, fizbo. To make them accessible to
   the VisIt team, you need to create a pull request.
4. Create a pull request
   * From your browser, go to
   [https://github.com/visit-dav/largedata/compare](https://github.com/visit-dav/largedata/compare)
   to create a pull request
   * Select the `compare across forks` text link and then select the repo you forked above from the list.
   * GitHub constructs a URL such as this
   [https://github.com/visit-dav/largedata/compare/master...fizbo:add-data-from-fizbo](https://github.com/visit-dav/largedata/compare/master...fizbo:add-data-from-fizbo)
   * Press the `Create pull request` button.
   * Once the last step is completed, the pull request, which includes the
   data file(s) you have added will be accessible to the VisIt team.
5. After whatever issues associated the data are resolved, VisIt team members
   will close the pull request.
