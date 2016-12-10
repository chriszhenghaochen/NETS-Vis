from bokeh.plotting import figure
from bokeh.models import Plot
from bokeh.properties import Instance
from bokeh.server.app import bokeh_app
from bokeh.server.utils.plugins import object_page
from bokeh.models.widgets import HBox, Button

class App(HBox):
    extra_generated_classes = [["App", "App", "HBox"]]
    plot = Instance(Plot)
    button = Instance(Button)

    @classmethod
    def create(cls):
        """One-time creation of app's objects.

        This function is called once, and is responsible for
        creating all objects (plots, datasources, etc)
        """
        obj = cls()

        plot = figure(x_range=(-2, 1), y_range=(-1, 1),
                      tools=[], plot_width=450,
                      plot_height=300, toolbar_location=None)
        plot.line([-0.5, 0.5], [-0.5, 0.5])
        obj.plot = plot
        button = Button(label='click!')
        obj.button = button
        obj.children.append(obj.plot)
        obj.children.append(obj.button)

        return obj

    def setup_events(self):
        super(App, self).setup_events()
        if not self.button:
            return
        self.button.on_click(self.click)

    def click(self, *args):
        print('***click***')


@bokeh_app.route("/bokeh/click")
@object_page("click")
def make_sliders():
    app = App.create()
    return app