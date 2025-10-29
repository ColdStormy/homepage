# My Homepage

This my own website which contains a quick introduction to my work profile, a gallery for my photos and showcasing/blogging personal projects I have.
WIP partially 🙂

Note, I am a CPP programmer. I up to no experience with a full web stack and some code here may be a little sloppy. I'm trying my best 💪

## 🏗️ Tech Stack

### Frontend
- **SvelteKit 2 (Svelte 5)** - Full-stack framework
- **TypeScript** - Type-safe development
- **TailwindCSS 4** - Utility-first styling
- **MDSveX** - Markdown support for content
- **Lucide** - SVG Icon Library

### Image Processing
- **Python** - Scripting and Image processing pipeline 
- **Pillow (PIL)** - Image manipulation and thumbnail generation

### Development Tools
- **Vite 7** - build tool and dev server
- **Sass** - Enhanced CSS preprocessing
- and a helping hand from **AI**

## 📁 Project Structure

```
├── src/
│   ├── routes/
│   │   ├── +layout.svelte          # Global layout
│   │   ├── +page.svelte            # Homepage
│   │   ├── publications/           # Academic publications
│   │   ├── projects/               # Project portfolio
│   │   └── sofortigramm/           # Photography gallery
│   │       ├── Gallery.svelte      # Main gallery component
│   │       ├── [imageID]/          # Individual image pages
│   │       └── +page.server.ts     # Server-side data loading
│   ├── lib/                        # Shared components and utilities
│   └── app.css                     # Global styles
├── static/
│   ├── images/
│   │   ├── database.json          # Image metadata
│   │   ├── thumbnails/            # Generated thumbnails
│   │   └── showcase/              # Optimized display images
│   └── files/                     # Static assets
├── assets/
│   └── original/                  # Original high-res images
└── scripts/
    └── createDatabase.py          # Image processing pipeline
```

## 🚀 Getting Started

### Prerequisites
- **Node.js** (v18+)
- **Python 3** (for image processing)
- **PowerShell** (Windows) or equivalent shell

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd homepage
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Process images** (if you have images in `assets/original/`)
   ```bash
   python scripts/createDatabase.py
   ```

5. **Start development server**
   ```bash
   npm run dev
   ```

## 📸 Photography Gallery (Sofortigramm)

Website is not going to work unless you have generated an image database (not stored in this repo by default).

### Adding New Images

1. Place high-resolution images in `assets/original/`
2. Run the processing script: `python scripts/createDatabase.py`
3. The script will automatically:
   - Generate thumbnails
   - Create showcase images (max FullHD resolution)
   - Update the JSON database with metadata
   - Maintain aspect ratios and quality

## 🛠️ Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run check` - Type checking
- `npm run format` - Format code with Prettier
- `npm run lint` - Lint code

## 📦 Deployment

The site is configured for static generation, so you can use files in `build/` on any hosting server.

```bash
npm run build
```

## 📄 License

© 2025 Jannis Bellok. All rights reserved.