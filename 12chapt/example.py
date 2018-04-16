from PyQt4 import QtGui, QtWebKit

app = QtGui.QApplication([])
view = QtWebKit.QWebView()

# intercept form submits
class MyWebPage(QtWebKit.QWebPage):
    def acceptNavigationRequest(self, frame, req, nav_type):
        if nav_type == QtWebKit.QWebPage.NavigationTypeFormSubmitted:
            text = "<br/>\n".join(["%s: %s" % pair for pair in req.url().queryItems()])
            view.setHtml(text)
            return False
        else:
            return super(MyWebPage, self).acceptNavigationRequest(frame, req, nav_type)
view.setPage(MyWebPage())

# setup the html form
html = """
<form action="" method="get">
Like it?
<input type="radio" name="like" value="yes"/> Yes
<input type="radio" name="like" value="no" /> No
<br/><input type="text" name="text" value="Hello" />
<input type="submit" name="submit" value="Send"/>
</form>
"""
view.setHtml(html)
