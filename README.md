## Welcome to Gcc's github project.
You can use the command('git clone' or 'git pull') to get source code[source code](https://github.com/CHINA-gcc/CHINA-gcc.github.io).

This github item mainly records some cases、basic code instructions and For reference only.

### Catalogs of Branch
- [master](https://github.com/CHINA-gcc/CHINA-gcc.github.io/tree/master)
- [DataBase](https://github.com/CHINA-gcc/CHINA-gcc.github.io/tree/Database)
- [Django_frame](https://github.com/CHINA-gcc/CHINA-gcc.github.io/tree/Django_frame)
- [Tornado_frame](https://github.com/CHINA-gcc/CHINA-gcc.github.io/tree/Tornado_frame)
- [Spider](https://github.com/CHINA-gcc/CHINA-gcc.github.io/tree/Spider)
### Git
- Global configuration
```python
> git config --global user.name '...'
> git config --global user.email '...'

Configure personal information to remove --global.
```
- Connection
```python
> git pull(execute command: git remote add <name,default is origin> <ssh_code>)
> git remote -v
>git remote rm <name, default is origin>         # Delete remote warehouse connections.
> git reflog(view history) | git log
```
- Branch
```python
> git branch -a(查看远程、本地分支)
> git checkout -b <本地分支, 创建并切换> | git branch <本地分支, 创建> | git checkout <本地分支, 创建>
> git push --set-upstream origin/<remote_branch_name> <local_branch_name>(设置远程为本地分支的 upstream-branch)
> git push <name, default is origin> <remote_branch_name>
> git reset --hard HEAD(current version) / HEAD^(脱字符) / 版本号
```
- Contrast
```python
> git diff HEAD --demo.py                      # Workspace with warehouse.
> git diff HEAD HEAD^ -- demo.py               # Local warehouse version codes.
```

### concluding remarks
