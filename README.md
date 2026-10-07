<div align="center">
  <img src="assets/header.svg" width="100%" alt="Russell Magdaong. I build games that teach things." />
  <br /><br />
  <a href="https://www.facebook.com/russssm"><img src="assets/btn-facebook.svg" height="40" alt="Facebook" /></a>
  <a href="mailto:russelldizonmagdaong@gmail.com"><img src="assets/btn-email.svg" height="40" alt="Email" /></a>
  <a href="https://russm.vercel.app"><img src="assets/btn-portfolio.svg" height="40" alt="Portfolio" /></a>
</div>

<br />

I'm a student developer from the Philippines and a DOST-SEI scholar. Most of what I build ends up being a game that teaches something: math, programming, or whatever I was struggling to learn at the time.

I like the part of a project where the "fun" layer and the "is this actually correct" layer have to meet. In practice that means a lot of Godot on the front and a lot of plain, deterministic code behind it.

I'm currently looking for a software engineering internship.

## What I've been building

### ODIN

<a href="https://insomnicode-odin.vercel.app"><img src="assets/odin.png" align="right" width="46%" alt="ODIN's battle screen, with a code editor next to the player character" /></a>

**A tutoring system disguised as a dungeon crawler.** ODIN is my undergraduate thesis, built with three teammates as InsomniCode. It teaches C# arrays through a pixel-art RPG: you walk a dungeon, run into an enemy, and win the fight by writing real code in an in-game editor.

The interesting part is what happens after you hit submit. The game records how you typed (pauses, bursts, how much you changed between attempts) and sends it with your code to an ASP.NET Core backend. Roslyn parses the code to find the specific misconception, such as an off-by-one loop bound, and Bayesian Knowledge Tracing estimates how well you know the skill. The typing data tells a student who is thinking apart from one who is guessing or stuck, and the hint you get depends on which one you are.

`Godot 4` `GDScript` `ASP.NET Core 8` `PostgreSQL` `React`

<a href="https://insomnicode-odin.vercel.app"><img src="assets/btn-play.svg" height="30" alt="Play ODIN" /></a> <a href="https://github.com/russellmagdaong/odin-game"><img src="assets/btn-source.svg" height="30" alt="ODIN game client source" /></a>

<br clear="both" />

### TAKO

<a href="https://github.com/russellmagdaong/tako-game"><img src="assets/tako.png" align="right" width="46%" alt="TAKO's opening area, a pixel-art billiard hall" /></a>

**A math RPG that works without internet.** TAKO is an Android game for Grades 7 to 10, aligned with the DepEd curriculum and playable in English or Filipino. It was built for students who don't have reliable internet, so everything runs from a local SQLite database and syncs to Supabase only when a connection exists.

Gemini writes the questions and the feedback, but it never grades anything. Answers are checked by ordinary code that knows `1/2`, `0.5` and `2/4` are the same number, and wrong answers are matched to known mistakes before the AI is asked to explain them. If the AI is unreachable, the game falls back to templates and keeps going.

`Godot 4` `GDScript` `SQLite` `Supabase` `Gemini 2.5 Flash`

<a href="https://github.com/russellmagdaong/tako-game"><img src="assets/btn-source.svg" height="30" alt="TAKO source" /></a>

<br clear="both" />

### Algebrawl

<a href="https://algebrawl.vercel.app"><img src="assets/algebrawl.png" align="right" width="46%" alt="Algebrawl's title screen" /></a>

**Turn-based fights against famous mathematicians.** This started as a Java Swing project for a college class. I later ported it to the web so people could play it without installing anything. You battle Gauss, Newton and Fibonacci by solving problems, with KaTeX rendering the math and the Web Audio API generating the sound effects.

The original Java version is still in the repo.

`React 19` `TypeScript` `Vite` `Tailwind CSS` `KaTeX`

<a href="https://algebrawl.vercel.app"><img src="assets/btn-play.svg" height="30" alt="Play Algebrawl" /></a> <a href="https://github.com/russellmagdaong/algebrawl"><img src="assets/btn-source.svg" height="30" alt="Algebrawl source" /></a>

<br clear="both" />

## Tools I reach for

<table>
  <tr>
    <td width="170"><b>Games</b></td>
    <td width="210"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/godot/godot-original.svg" height="28" alt="Godot" title="Godot" /></td>
    <td>Godot 4, GDScript</td>
  </tr>
  <tr>
    <td width="170"><b>Web</b></td>
    <td width="210"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/typescript/typescript-original.svg" height="28" alt="TypeScript" title="TypeScript" />&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg" height="28" alt="React" title="React" />&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vitejs/vitejs-original.svg" height="28" alt="Vite" title="Vite" />&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tailwindcss/tailwindcss-original.svg" height="28" alt="Tailwind CSS" title="Tailwind CSS" /></td>
    <td>TypeScript, React, Vite, Tailwind CSS</td>
  </tr>
  <tr>
    <td width="170"><b>Backend and data</b></td>
    <td width="210"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/csharp/csharp-original.svg" height="28" alt="C#" title="C#" />&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/dotnetcore/dotnetcore-original.svg" height="28" alt="ASP.NET Core" title="ASP.NET Core" />&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" height="28" alt="PostgreSQL" title="PostgreSQL" />&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original.svg" height="28" alt="SQLite" title="SQLite" />&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/supabase/supabase-original.svg" height="28" alt="Supabase" title="Supabase" /></td>
    <td>C#, ASP.NET Core, PostgreSQL, SQLite, Supabase</td>
  </tr>
  <tr>
    <td width="170"><b>Also comfortable in</b></td>
    <td width="210"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg" height="28" alt="Java" title="Java" />&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="28" alt="Python" title="Python" />&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg" height="28" alt="C++" title="C++" /></td>
    <td>Java, Python, C++</td>
  </tr>
</table>

## Other things

- DOST-SEI Scholar
- PMI Project Management Ready, Project Management Institute
- Python developer certification

<br />

<div align="center">
  <sub>The header is ODIN's in-game dialogue box. Pixel font: PIXY by 2DFUNS Studio (CC BY 3.0).</sub>
</div>
