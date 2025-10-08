<script>
	import { Segment } from '@skeletonlabs/skeleton-svelte';
	import { MoveLeft } from '@lucide/svelte';
	import Gallery from './Gallery.svelte';	
	import ScrollTopButton from './ScrollTopButton.svelte';
</script>

<section
	class="relative flex flex-col items-center justify-center min-h-screen py-16 px-4"
>
	<div class="w-full xl:w-2/3">
		<h1 class="text-4xl font-bold text-center mb-8">Sofortigramm</h1>

		<div class="w-full text-justify px-10">
			<p>
				A small text about the gallery and the photos. This gallery showcases a collection of stunning images from various categories including landscapes, architecture, nature, and more. Use the filters below to explore different themes and styles.
			</p>

			<br />
			<a href="/" class="anchor align-baseline">
				<MoveLeft size="16" strokeWidth={2} class="inline-flex gap-1 align-text-middle" />
				Back to Home
			</a>
		</div>

		<div class="flex flex-row justify-start items-start gap-4 p-10 transition-transform">
			<Gallery />
		</div>
	</div>
</section>

<ScrollTopButton />