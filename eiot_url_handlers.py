import re
import terminatorlib.plugin as plugin

# Every plugin you want Terminator to load *must* be listed in 'AVAILABLE'
AVAILABLE = ['JiraEIoTURLHandler']

class JiraEIoTURLHandler(plugin.URLHandler):
    capabilities = ['url_handler']
    handler_name = 'launchpad_bug'
    match = 'EIOT-[0-9]+'
    nameopen = "Open EIoT Jira ticket"
    namecopy = "Copy URL"

    def callback(self, url):
        """Look for the number in the supplied string and return it as a URL"""
        url_ = 'https://jira.%%62it%%64efender.biz/browse/%s' % url
        return(url_)
