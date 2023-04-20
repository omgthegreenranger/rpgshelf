# Main code for running the tagger itself.

# Directory/File select
# Begin URL preparation


# Initial Search Program

import getFiles
# import pdfreader

args = {}
sel = 1

# pdfreader.pdfsearch()
# print(pdfreader.qsearchterms)
result = getFiles.apiSearch(args)
# rpg_selector = getFiles.apiSelect()
print(result)