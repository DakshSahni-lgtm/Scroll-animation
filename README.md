# Frame-by-Frame Scroll Animation

Turn any sequence of images into a smooth, scroll-driven animation — like the product reveals you see on Apple's website.

---

## How It Works

As the user scrolls down the page, JavaScript swaps canvas frames in sync with their scroll position. The result feels like a 3D animation, but it's just a sequence of `.jpg` images played one at a time.

---

## Quick Start

### 1. Collect Frames From Your Video

Use any frame extractor tool.
> BONUS: You can use my frame extractor tool for generating upto 60 frames per second without any quality loss: [video-frames-extractor](https://dakshsahni14.github.io/video-frames-extractor/) .

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

## Does Frame Count Affect Page Height?
 
**No.** You do not need to change `height: 400vh`, the canvas size, or anything else when you change the number of frames.
 
The animation always plays across the full scroll range, regardless of how many frames there are. The math is proportional:
 
```
scroll 0% → frame 1
scroll 50% → middle frame
scroll 100% → last frame
```
 
More frames just means a smoother animation — each frame gets a smaller slice of the same scroll distance. The only reason to increase `400vh` is if you want the user to scroll *longer* before the animation finishes. That's a creative choice, not a technical one.
 
---
 
## My Frames Are a Different Aspect Ratio
 
By default, the canvas stretches each frame to fill the entire screen. If your frames are 16:9 but the viewer's screen is portrait (like a phone), the image will look squashed — and vice versa.
 
The fix is to replace the two `context.drawImage(...)` lines in `index.html` with a smarter version that scales the frame to fill the screen without distorting it (cropping the edges slightly instead, just like a full-screen photo wallpaper).
 
**Step 1** — Find this block near the bottom of `index.html` and delete it:
 
```js
images[0].onload = () => {
    context.drawImage(images[0], 0, 0, canvas.width, canvas.height);
}
```
 
Replace it with:
 
```js
images[0].onload = () => {
    drawFrame(images[0]);
}
```
 
**Step 2** — Find this line inside the scroll listener and delete it:
 
```js
context.drawImage(images[frameIndex], 0, 0, canvas.width, canvas.height);
```
 
Replace it with:
 
```js
drawFrame(images[frameIndex]);
```
 
**Step 3** — Add this new function anywhere in the `<script>`, before the scroll listener:
 
```js
function drawFrame(img) {
    const canvasRatio = canvas.width / canvas.height;
    const imgRatio = img.naturalWidth / img.naturalHeight;
    let drawWidth, drawHeight, offsetX, offsetY;
 
    if (imgRatio > canvasRatio) {
        drawHeight = canvas.height;
        drawWidth = drawHeight * imgRatio;
    } else {
        drawWidth = canvas.width;
        drawHeight = drawWidth / imgRatio;
    }
 
    offsetX = (canvas.width - drawWidth) / 2;
    offsetY = (canvas.height - drawHeight) / 2;
 
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.drawImage(img, offsetX, offsetY, drawWidth, drawHeight);
}
```
 
That's it. This works for any ratio — 16:9, 9:16, 1:1, or anything else.
 
> **Which ratio should I export my frames in?**
> - Making a **desktop site**? Use 16:9 (e.g. 1920×1080).
> - Making a **mobile site**? Use 9:16 (e.g. 1080×1920).
> - Want it to **work on both**? Use 9:16. The fix above will crop the left and right edges slightly on desktop, which usually looks fine as long as your subject is centred in the frame.
 
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
