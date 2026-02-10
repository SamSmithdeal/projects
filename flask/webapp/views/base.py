from flask_appbuilder import BaseView, expose
from markdown import markdown
from pathlib import Path

def md_to_html(filename: str) -> str:
    """Render a markdown file as html."""
    path = Path("templates") / filename
    text = path.read_text(encoding="utf-8")
    return markdown(text, extensions=["attr_list"])


class AboutView(BaseView):
    route_base = "/about"

    @expose("/")
    def about(self):
        return self.render_template("about.jinja", content=md_to_html("about.md"))