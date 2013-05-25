from subprocess import call
import sys


def main():
    if len(sys.argv) == 2:
    	call('gist ' + sys.argv[1], shell=True)
    	call('python /home/joe/Documents/workstage/joelewis/blog/utils/addone.py', shell=True)
        call('git --git-dir=/home/joe/Documents/workstage/joelewis/.git --work-tree=/home/joe/Documents/workstage/joelewis  add .',shell=True)
        call('git --git-dir=/home/joe/Documents/workstage/joelewis/.git --work-tree=/home/joe/Documents/workstage/joelewis commit -m "+1 post"',shell=True)
        call('git --git-dir=/home/joe/Documents/workstage/joelewis/.git --work-tree=/home/joe/Documents/workstage/joelewis push heroku master', shell=True)
    else:
      print "enter valid filename"    
if  __name__ =='__main__':
    main()