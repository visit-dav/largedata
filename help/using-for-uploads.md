## Options for uploading large files

If a user needs to get data to VisIt developers for any reason,
the options available depend on the size of the files. In all of
the scenarios below, compression can help mitgate size limits.
If you have easy access to [7zip](7zip.md) compression tools, it
can often yield the best compression by sometimes a factor of 2-3x.
In addition, to simplify handling of potentially many files, it is
best to use an [*archiver*](https://en.wikipedia.org/wiki/File_archiver)
tool such as `tar`, `zip`, `7z`, etc.

* Email to an individual developer
  * **Size Limit: 5-10 MB**
  * The actual size limit depends on several factors which are likely outside
    the knowledge of sender and recipeint.
  * Our cyber-filtering will remove file attachments with certain extensions.
  If this is an issue, try adding a funky file extension like `.gorfo`
  (e.g. name your attachment `foo.tar.gz.gorfo` instead of `foo.tar.gz`).
* Attachments to [Discussions](https://github.com/visit-dav/visit/discussions)
  * Only certain file extensions are supported.
  * **Size Limits:**
    * **Image files (`.gif`., `.png`, `.jpeg` and `.jpg`) < 10MB.**
    * **Raw text files (`.txt`, and `.log`) < 25MB.**
    * **Document files (`.pdf`, `.docx`, `.pptx`, and `.xlsx`) < 25MB.**
    * **Compressed files (`.gz`, `.zip`) < 25MB.**
  * Because GitHub currently keys off only the file's extension, you can
  attach any format by simply spoofing the extension. For example, to
  attach `foo.obj` just rename it to `foo.obj.not.gz`. Or, better yet, just
  compress `foo.obj` with gzip to produce `foo.obj.gz`.
* [LLNL Anonymous FTP server](https://hpc.llnl.gov/sites/default/files/anonymousFTPinstructions.pdf), ftp://ftp.llnl.gov
  * **Size limit:  probably < 1GB**
  * Works only to get data to VisIt developers with LLNL accounts.
  * It is not possible to use a web browser to upload data to ftp://ftp.llnl.gov.
    Only command-line FTP tools that do not attempt to show directory listings will work.
  * Uploaders need to upload their files to the `incoming` directory on the server.
    * **Note:** VisIt developers may also *download* data to users via the `outgoing`
      directory.
  * Whether uploading or downloading data via ftp.llnl.gov, everyone needs to know
    the full URLs of the associated files in order to access them.
  * Using the standard ftp command-line tool...
    ```
    % ftp ftp.llnl.gov
    % Connected to ftp.llnl.gov.
    220-        **WARNING**WARNING**WARNING**WARNING**WARNING**
    220-        
    220- This is a Department of Energy (DOE) computer system. DOE
    .
    .
    .
    Name (ftp.llnl.gov:<someuser>): anonymous
    331 Please specify email address as password.
    Password:
    230 Login successful.
    Remote system type is UNIX.
    Using binary mode to transfer files.
    Unknown command.
    ftp> bin # Switch data mode to binary when sending binary (e.g. not ascii) files
    200 Switching to Binary mode.
    ftp> cd incoming
    ftp> put foo.tar.gz someuser-upload-1.tar.gz # be sure to create a likely unique file name on the server
    local: foo.tar.gz remote: someuser-upload-1.tar.gz
    500 Unknown command.
    ALLO64 83 - command not accepted - Reverting to ALLO command
    200 The filesize has been allocated.
    200 PORT command successful. Consider using PASV.
    150 Ok to send data.
    226 Transfer complete.
    443 bytes sent in 0.0075 seconds (0.011 MBytes/sec)
    ftp> ctrl-D
    ftp> 221 Goodbye.
    ```
  * Using `curl`
    ```
    curl -T foo.tar.gz --ftp-create-dirs ftp://ftp.llnl.gov/incoming/someuser/upload-1.tar.gz
    ```
    **Note:** the command above also demonstrates the creation of a new directory in the
    ftp server's `incoming` directory using curl. We currently know of no way to use `wget` to
    in the same way.
  * Email VisIt developers with the *full* URL name(s) of the files you uploaded there
    so they know to go get them. For example...
    ```
    ftp://ftp.llnl.gov/incoming/someuser/upload-1.tar.gz
    ```
  * Files uploaded there are readable only from LLNL firewalled networks and are
    purged regularly.
* Submit a PR from a [fork of this repository](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
  * [**Size limit: < 2GB**](https://help.github.com/en/github/managing-large-files/about-git-large-file-storage)
  * Works for *any* VisIt developer
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
