# Astrobotany

![Astrobotany](https://github.com/michael-lazar/astrobotany/workflows/Astrobotany/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A community garden over the [gemini](https://gemini.circumlunar.space/) protocol. Fork of [jifunks/botany](https://github.com/jifunks/botany).

---

<p align="center">
    🌱&nbsp;•&nbsp;🛰️&nbsp;•&nbsp;🌷&nbsp;•&nbsp;🐝&nbsp;•&nbsp;🚀&nbsp;•&nbsp;🌵&nbsp;•&nbsp;👩‍🚀
    <strong><a href="gemini://astrobotany.mozz.us">gemini://astrobotany.mozz.us</a></strong>
    <a href="https://portal.mozz.us/gemini/astrobotany.mozz.us/">(http&nbsp;proxy)</a>
    🥕&nbsp;•&nbsp;🔭&nbsp;•&nbsp;🌺&nbsp;•&nbsp;👩‍🔬&nbsp;•&nbsp;🌍&nbsp;•&nbsp;👨‍🌾&nbsp;•&nbsp;🌧️
</p>

---

<p align="center">
  <img alt="screen1" src="screenshots/screen1.png"/>
  <img alt="screen2" src="screenshots/screen2.png"/>
</p>

## Development Quickstart

### 1. Install

```
git clone git@github.com:michael-lazar/astrobotany.git
cd astrobotany
python3 -m virtualenv venv

source venv/bin/activate
pip install -e .

# Generate a self-signed CA
./scripts/generate_server_ca.sh

# Add a handful of test users
./scripts/add_seed_data.py 10
```

### 2. Run

```
source venv/bin/activate
python main.py
```

### 3. Connect

```
# Generate a signed client certificate
./scripts/generate_client_cert.sh test_user

# Using https://tildegit.org/solderpunk/AV-98
av98 gemini://localhost --tls-cert certs/test_user.cer --tls-key certs/test_user.key
```

## Art

### Gallery

**[View Plant Screenshots](GALLERY.md)**

### Playscii

I use a forked version of the playscii ASCII art program to generate the ``.psci`` files:

https://github.com/michael-lazar/playscii

Botany's original art files were imported using the following settings:

- palette: ``240-ansi`` (generated using [this script](scripts/build_palette.py))
- charset: ``dos`` (of which 7-bit US ASCII is a subset)

I intentionally excluded colors 0-15 from the palette because those colors can
be modified by a user's terminal theme, and I want total control of the
final rendered text.

When colorizing, I maintained a few common colors between plants:

| Color Code | Usage |
| --- | --- |
| 0 | background |
| 80 | soil |
| 133 | primary flower color |
| 199 | secondary flower color |
