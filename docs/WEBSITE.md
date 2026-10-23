# Website preview and GitHub Pages

The first interactive website prototype lives in the repository root:
- `index.html`
- `assets/css/site.css`
- `assets/js/app.js`
- `data/index.json`

It reads the JSON registry at runtime and provides search, media filters, topic shortcuts, character detail dialogs, and journey exploration. Cards use original abstract gradient artwork rather than unlicensed poster images.

## Preview locally

Because the site loads JSON with `fetch()`, open it through a local static server rather than double-clicking the HTML file.

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Enable GitHub Pages

The repository is currently private and GitHub Pages has not been enabled. The deployment workflow cannot publish until the repository has a Pages site configured. Do not make the repository public just to preview the design.

If your GitHub plan supports Pages for a private repository, open **Settings → Pages**, choose **GitHub Actions** as the build and deployment source, and rerun the Pages workflow. If private-repository Pages is not available on your plan, keep the repository private and use a local preview or choose an approved public hosting option after deciding what data should be public.

The Pages workflow is separate from the data validation workflow. A successful data validation does not mean the public site is deployed.
