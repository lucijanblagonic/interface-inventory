# Author: Nikola Plejic, github.com/nikolaplejic

import sys
import os

if len(sys.argv) < 2:
    print "I can haz argument?"
    exit()

extension_templates = {
    "html": "<!-- %s -->\n\n%s",
    "kit": "<!-- %s -->\n\n%s",
    "php": "<!-- %s -->\n\n%s",
    "css": "/* %s */\n\n%s",
    "scss": "/* %s */\n\n%s",
    "less": "/* %s */\n\n%s",
    "js": "/* %s */\n\n%s",
}

csv_separator = ","
file_ext_separator = "|"
build_folder = "build"

opts = open(sys.argv[1]).readlines()

try:
    os.mkdir(build_folder)
except OSError, e:
    print "%s/ folder exists, continuing..." % build_folder

for opt in opts:
    # assumption:
    # elements[0] = title
    # elements[1] = filename
    # elements[2] = file extensions (pipe separated)
    # elements[3] = description
    elements = opt.split(csv_separator)
    exts = [ x for x in elements[2].split(file_ext_separator)
             if x in extension_templates.keys() ]

    for e in exts:
        file_name = "%s/_%s.%s" % (build_folder, elements[1], e)
        file_contents = extension_templates[e] % (elements[0], elements[3])
        with open(file_name, "w") as outfile:
            outfile.write(file_contents)