import { mdsvex } from 'mdsvex';
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations
	// for more information about preprocessors
	preprocess: [vitePreprocess({script: true}), mdsvex()],
	kit: { 
		adapter: adapter(),
		alias: {
			"database.json": "static/images/database.json"
		}
	 },
	extensions: ['.svelte', '.svx']
};

export default config;
