# Frame-by-Frame Scroll Animation

Turn any sequence of images into a smooth, scroll-driven animation — like the product reveals you see on Apple's website.

---

## How It Works

As the user scrolls down the page, JavaScript swaps canvas frames in sync with their scroll position. The result feels like a 3D animation, but it's just a sequence of `.jpg` images played one at a time.

---

## Quick Start

### 1. Collect Frames From Your Video

Use any frame extractor tool.
> BONUS: You can use my frame extractor tool for generating upto 60 frames per second without any quality loss: [video-frames-extractor](https://dakshsahni-lgtm.github.io/video-frames-extractor/) .

### 2. Prepare Your Frames

Create a folder named `frames` in the same directory as `index.html`:

```
your-project/
├── index.html
├── rename.py        ← optional helper script
└── frames/
    ├── 0001.jpg
    ├── 0002.jpg
    ├── 0003.jpg
    └── ...
```

Frames must be named sequentially: `0001.jpg`, `0002.jpg`, … up to your last frame (e.g. `0087.jpg`).

> **Tip:** Export frames from video editing software like Adobe Premiere, After Effects, or DaVinci Resolve. Most apps let you export as an image sequence directly.

---

### 3. Update the Frame Count

Open `index.html` and find this line near the top of the `<script>`:

```js
const frameCount = 65;
```

Change `65` to however many frames you have. For example, if your last file is `0087.jpg`:

```js
const frameCount = 87;
```

---

### 4. Open in a Browser

Open `index.html` in your browser and scroll — you should see your animation play.

> ⚠️ **Important:** Open it through a local server, not by double-clicking the file. Browsers block local file loading by default.
>
> Easy options:
> - **VS Code** → install the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension, then click "Go Live"
> - **Python** → run `python -m http.server` in your project folder, then visit `http://localhost:8000`

---

## Can't Rename All Your Frames Manually?

Use the included `rename.py` script. It automatically renames all image files in your `frames/` folder to the correct `0001.jpg`, `0002.jpg`, … format.

```bash
python rename.py
```

Run it from your project's root directory (where `index.html` lives). It will sort your existing files alphabetically and rename them in order.

---

## Customisation

| What to change | Where |
|---|---|
| Scroll distance (how long the animation takes) | `height: 400vh` in the CSS `body` rule — increase for a slower reveal |
| Number of frames | `const frameCount = 65` in the script |
| Frame folder or file format | `const currentFrame = index => ...` in the script |

---

## Troubleshooting

**Blank canvas / no animation**
- Make sure you're using a local server (see Step 3 above)
- Check that your `frames/` folder is in the same directory as `index.html`
- Confirm filenames start at `0001.jpg`, not `0000.jpg`

**Animation is choppy**
- Reduce image resolution — frames don't need to be larger than your screen
- Use compressed JPEGs; a quality of 70–80% is usually indistinguishable and loads much faster

**Frame count looks wrong**
- Double-check that `frameCount` matches the number of files in your `frames/` folder exactly
