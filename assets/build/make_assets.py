"""Builds the SVGs used by the profile README: the dialogue-box header and the buttons.

Text is drawn as outlines taken from the PIXY pixel font, so the images look the
same on every machine and need no font loading. Edit the text below, then run:

    python assets/build/make_assets.py

Requires: pip install fonttools
"""
import base64
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

HERE = Path(__file__).parent
OUT = HERE.parent

NAME = "Russell Magdaong"
ROLE = "Student developer / DOST-SEI scholar / Philippines"
LINES = [
    "I build games that teach things.",
    "Godot up front, plain code behind it.",
    "Now building ODIN, a tutor that lives inside a dungeon crawler.",
    "Looking for a software engineering internship.",
]

# Colours lifted from ODIN's in-game dialogue box.
PANEL = "#21252e"
INSET = "#171a21"
BORDER = "#1e90ff"
CYAN = "#00ffff"
WHITE = "#ffffff"
MUTED = "#9aa7bd"

SECONDS_PER_LINE = 5.5
SECONDS_PER_CHAR = 0.035

ICONS = {
    "linkedin": '<path transform="scale(.8333)" d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>',
    "facebook": '<path transform="scale(.8333)" d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>',
    "email": '<g fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"><rect x="1.5" y="3.5" width="17" height="13" rx="1.5"/><path d="M2 5l8 6 8-6"/></g>',
    "portfolio": '<g fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"><rect x="1.5" y="2.5" width="17" height="15" rx="1.5"/><path d="M2 7.5h16"/></g>',
    "play": '<path d="M5 2.5l12 7.5-12 7.5z"/>',
    "source": '<path fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="square" d="M7 5l-5 5 5 5M13 5l5 5-5 5"/>',
}


class Canvas:
    """Collects the glyph outlines one SVG needs and lays text out with them."""

    def __init__(self):
        self.font = TTFont(HERE / "PIXY.ttf")
        self.cmap = self.font.getBestCmap()
        self.glyphs = self.font.getGlyphSet()
        self.upm = self.font["head"].unitsPerEm
        self.defs = {}

    def width(self, text, size):
        return sum(self.glyphs[self.cmap[ord(c)]].width for c in text) * size / self.upm

    def text(self, text, x, y, size, fill, anchor="start", char_attrs=None):
        """Returns <use> elements for `text` with its baseline starting at (x, y)."""
        if anchor == "end":
            x -= self.width(text, size)
        elif anchor == "middle":
            x -= self.width(text, size) / 2
        scale = size / self.upm
        uses, pen_x = [], 0
        for i, ch in enumerate(text):
            name = self.cmap[ord(ch)]
            if ch != " ":
                if name not in self.defs:
                    pen = SVGPathPen(self.glyphs)
                    self.glyphs[name].draw(pen)
                    self.defs[name] = (f"g{ord(ch)}", pen.getCommands())
                extra = f" {char_attrs(i)}" if char_attrs else ""
                uses.append(f'<use href="#{self.defs[name][0]}" x="{pen_x}"{extra}/>')
            pen_x += self.glyphs[name].width
        return (
            f'<g transform="translate({x:.1f} {y}) scale({scale:.5f} -{scale:.5f})" fill="{fill}">'
            + "".join(uses)
            + "</g>"
        )

    def wrap(self, text, size, max_width):
        lines, current = [], ""
        for word in text.split():
            trial = f"{current} {word}".strip()
            if current and self.width(trial, size) > max_width:
                lines.append(current)
                current = word
            else:
                current = trial
        return lines + [current]

    def glyph_defs(self):
        return "<defs>" + "".join(f'<path id="{i}" d="{d}"/>' for i, d in self.defs.values()) + "</defs>"


def header():
    c = Canvas()
    w, h = 860, 220
    text_x, text_right = 178, 836
    cycle = SECONDS_PER_LINE * len(LINES)
    line_pct = (SECONDS_PER_LINE - 0.3) / cycle * 100
    char_pct = SECONDS_PER_LINE / cycle * 100

    body = [
        f'<rect x="2" y="2" width="{w - 4}" height="{h - 4}" rx="8" fill="{PANEL}" stroke="{BORDER}" stroke-width="4"/>',
        f'<rect x="22" y="22" width="132" height="176" rx="6" fill="{INSET}" stroke="{BORDER}" stroke-width="3"/>',
    ]
    sprite = base64.b64encode((HERE / "player.png").read_bytes()).decode()
    body.append(f'<image href="data:image/png;base64,{sprite}" x="44" y="26" width="88" height="168"/>')
    body.append(c.text(NAME, text_x, 66, 40, CYAN))
    body.append(c.text(ROLE, text_x, 95, 17, MUTED))

    for n, line in enumerate(LINES):
        start = n * SECONDS_PER_LINE
        typed = 0
        rows = []
        for row, part in enumerate(c.wrap(line, 24, text_right - text_x)):
            def delay(i, typed=typed):
                return f'class="c" style="animation-delay:{start + 0.25 + (typed + i) * SECONDS_PER_CHAR:.2f}s"'

            rows.append(c.text(part, text_x, 138 + row * 30, 24, WHITE, char_attrs=delay))
            typed += len(part) + 1
        body.append(f'<g class="m m{n}" style="animation-delay:{start}s">' + "".join(rows) + "</g>")

    body.append(f'<g opacity=".55">{c.text("[Enter]/[Click] Next", text_right, 200, 14, WHITE, anchor="end")}</g>')
    hint_x = text_right - c.width("[Enter]/[Click] Next", 14) - 18
    body.append(f'<path class="nx" d="M{hint_x:.1f} 189h10l-5 8z" fill="{CYAN}"/>')

    css = (
        f".m{{opacity:0;animation:m {cycle}s steps(1,end) infinite}}"
        f".c{{opacity:0;animation:c {cycle}s steps(1,end) infinite}}"
        f"@keyframes m{{0%{{opacity:1}}{line_pct:.2f}%{{opacity:0}}100%{{opacity:0}}}}"
        f"@keyframes c{{0%{{opacity:1}}{char_pct:.2f}%{{opacity:0}}100%{{opacity:0}}}}"
        ".nx{animation:nx 1s steps(1,end) infinite}"
        "@keyframes nx{0%{opacity:1}50%{opacity:0}100%{opacity:0}}"
        "@media (prefers-reduced-motion:reduce){.m,.c,.nx{animation:none}.m0,.m0 .c{opacity:1}}"
    )
    label = f"{NAME}. " + " ".join(LINES)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">'
        f"<title>{label}</title><style>{css}</style>{c.glyph_defs()}{''.join(body)}</svg>"
    )
    (OUT / "header.svg").write_text(svg, encoding="utf-8")


def button(filename, label, icon, dimmed=False):
    c = Canvas()
    h, size, pad = 44, 19, 15
    w = round(pad + 20 + 10 + c.width(label, size) + pad)
    text = c.text(label, pad + 30, 29, size, WHITE)
    dash = ' stroke-dasharray="6 5"' if dimmed else ""
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">'
        f"<title>{label}</title>{c.glyph_defs()}"
        f'<rect x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="6" fill="{PANEL}" stroke="{BORDER}" stroke-width="3"{dash}/>'
        f'<g opacity="{0.55 if dimmed else 1}"><g transform="translate({pad} 12)" fill="{WHITE}">{ICONS[icon]}</g>{text}</g>'
        "</svg>"
    )
    (OUT / filename).write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    header()
    button("btn-linkedin.svg", "LinkedIn", "linkedin")
    button("btn-facebook.svg", "Facebook", "facebook")
    button("btn-email.svg", "Email", "email")
    button("btn-portfolio.svg", "Portfolio: soon", "portfolio", dimmed=True)
    button("btn-play.svg", "Play it", "play")
    button("btn-source.svg", "Source", "source")
