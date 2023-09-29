from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        
        environ = self.loader.loadModel("models/environment")
        environ.setScale(0.25, 0.25, 0.25)
        environ.reparentTo(self.render)

app = MyApp()
app.run()
