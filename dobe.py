from optparse import OptionParser
from dobe_api import *
from dobe_view import *

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-c", "--console",
                  action="store_true", dest="consolemode", default=False,
                  help="run in console only mode")

    (options, args) = parser.parse_args()

    api = Dobe_API()
    http = Dobe_API_HTTP(api)

    if options.consolemode:
        input('Press Enter to exit')
    else:
        Dobe_View()