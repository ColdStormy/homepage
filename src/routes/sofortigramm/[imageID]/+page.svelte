<script lang="ts">
	import type { PageProps } from './$types';
	import { Camera, Aperture, Clock, Zap, Info } from '@lucide/svelte';

	let { data }: PageProps = $props();
	const imageID = data.post.imageID;
	
	// Generate consistent image data based on imageID
	const imageNumber = parseInt(imageID.replace('coldstormy', '')) || 1;
	const seed = imageNumber;
	
	// Generate consistent dimensions
	const height = Math.floor(Math.sin(seed) * 100) + 600; // Height between 500-700
	const width = Math.floor(Math.cos(seed) * 200) + 800; // Width between 600-1000
	
	const imageData = {
		src: `https://picsum.photos/seed/${imageID}/${width}/${height}`,
		title: [
			'Serene Mountain Landscape',
			'Urban Architecture Study',
			'Golden Hour Portrait',
			'Abstract Light Patterns',
			'Street Life Moments',
			'Natural Textures'
		][imageNumber % 6]
	};

	// Generate consistent camera data
	const cameras = ['Canon EOS R5', 'Sony A7R IV', 'Nikon D850', 'Fujifilm X-T4', 'Leica Q2'];
	const lenses = ['24-70mm f/2.8', '85mm f/1.4', '16-35mm f/2.8', '50mm f/1.2', '35mm f/1.4'];
	const apertures = ['f/2.8', 'f/1.4', 'f/4.0', 'f/5.6', 'f/8.0'];
	const shutterSpeeds = ['1/125s', '1/250s', '1/60s', '1/500s', '1/1000s'];
	const isos = ['ISO 100', 'ISO 200', 'ISO 400', 'ISO 800', 'ISO 1600'];

	const cameraDetails = {
		camera: cameras[imageNumber % cameras.length],
		lens: lenses[imageNumber % lenses.length],
		aperture: apertures[imageNumber % apertures.length],
		shutterSpeed: shutterSpeeds[imageNumber % shutterSpeeds.length],
		iso: isos[imageNumber % isos.length],
		dateTaken: new Date(2024, (imageNumber % 12), (imageNumber % 28) + 1).toLocaleDateString('en-US', {
			year: 'numeric',
			month: 'long',
			day: 'numeric'
		})
	};

	let imageLoaded = $state(false);
	
	const handleImageLoad = () => {
		imageLoaded = true;
	};
</script>

<svelte:head>
	<title>{imageData.title} - Photography Portfolio</title>
	<meta name="description" content={imageData.description} />
</svelte:head>

<div class="w-full flex items-center justify-center">
	<div class="relative h-full max-w-7xl mx-auto bg-white">
		{#if !imageLoaded}
			<div class="h-full aspect-[3/2] animate-pulse flex items-center justify-center">
				<div>Loading image...</div>
			</div>
		{/if}
		
		<img
			src={imageData.src}
			alt={imageData.title}
			class="h-full w-auto object-cover shadow-2xl"
			class:opacity-0={!imageLoaded}
			class:opacity-100={imageLoaded}
			style="transition: opacity 0.5s ease-in-out;"
			onload={handleImageLoad}
		/>
	</div>
</div>

<!-- Content Section -->
<div class="max-w-4xl mx-auto px-6 py-12 space-y-8">
	<div class="preset-filled-primary-950-50 rounded-lg p-6">
		<h2 class="text-2xl font-semibold mb-6 flex items-center gap-2">
			{imageData.title}
		</h2>
		
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
			<div class="flex items-center gap-3">
				<Camera size="20" class="" />
				<div>
					<div class="text-sm">Camera</div>
					<div class="font-medium">{cameraDetails.camera}</div>
				</div>
			</div>
			
			<div class="flex items-center gap-3">
				<Info size="20" class="" />
				<div>
					<div class="text-sm">Lens</div>
					<div class="font-medium">{cameraDetails.lens}</div>
				</div>
			</div>
			
			<div class="flex items-center gap-3">
				<Aperture size="20" class="" />
				<div>
					<div class="text-sm">Aperture</div>
					<div class="font-medium">{cameraDetails.aperture}</div>
				</div>
			</div>
			
			<div class="flex items-center gap-3">
				<Clock size="20" class="" />
				<div>
					<div class="text-sm">Shutter Speed</div>
					<div class="font-medium">{cameraDetails.shutterSpeed}</div>
				</div>
			</div>
			
			<div class="flex items-center gap-3">
				<Zap size="20" class="" />
				<div>
					<div class="text-sm">ISO</div>
					<div class="font-medium">{cameraDetails.iso}</div>
				</div>
			</div>
			
			<div class="flex items-center gap-3">
				<Info size="20" class="" />
				<div>
					<div class="text-sm">Date Taken</div>
					<div class="font-medium">{cameraDetails.dateTaken}</div>
				</div>
			</div>
		</div>
	</div>

	<!-- Additional Info -->
	<div class="border-t pt-8">
		<div class="text-center space-y-4">
			<p class="">
				Image ID: <span class="badge preset-filled-primary-950-50">{imageID}</span>
			</p>
		</div>
	</div>
</div>