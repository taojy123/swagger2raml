# swagger2raml
convert swagger json data to raml



Usage
----------------------------------

    $ git clone https://github.com/taojy123/swagger2raml
    $ cd swagger2raml
    $ python s2r.py
    ...
    Finish!
	$ cd ./result/
	$ ls
	aaa.raml       bbb.raml       ccc.raml  ...


See help for general options:

    $ python s2r.py --help
	Usage:   
	  python s2r.py [options]
	
	General Options:
	  -h, --help                    Show help.
	  -i(--input=) <api_root_url>   Such as: 'http://xxx.com/api/docs/api-docs/'
	  -o(--output=) <result_dir>    Such as: './result/'
	  -t(--title=) <title_prefix>   Such as: 'My_First_Api'
	  -p(--patches=) <patch_files>  Such as: 'aaa.raml,patches/bbb.raml,ccc.raml'
	
