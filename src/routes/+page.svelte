<script>
	const greetings = ['Hello there'];
	const greeting = greetings[Math.floor(Math.random() * greetings.length)];
</script>

<section
	class="relative flex flex-col items-center justify-center min-h-screen px-4 overflow-hidden font-sans text-gray-200 pt-20"
>
	<div class="fixed inset-0 w-screen h-screen z-0">
		<picture class="w-full h-full block">
			<!-- Tablet (medium) -->
			<source media="(min-width:768px)" srcset="/images/bg-wide.jpg" />
			<!-- Mobile (small) -->
			<source media="(max-width:767px)" srcset="/images/bg-mobile.jpg" />
			<!-- Fallback image for browsers that don't support <picture> -->
			<img
				src="/images/DSC00048_DxO.jpg"
				alt="Background"
				class="object-cover w-full h-full"
				loading="lazy"
				decoding="async"
			/>
			<div
				class="absolute inset-0 bg-gradient-to-b from-black/60 to-zinc-900/80 bg-linear-to-r/srgb"
			>
				<div class="w-full h-full backdrop-blur-xs"></div>
			</div>
		</picture>
	</div>
	<div class="flex flex-col z-10 max-w-2xl w-full text-center">
		<h1 class="text-6xl font-bold mb-2 text-white drop-shadow">{greeting}</h1>
		<div class="h-20 w-24 bg-transparent mx-auto mb-4 rounded"></div>
		<p class="text-lg mb-6 drop-shadow">
			At home I build software <br />
			On vacation, I chase light and landscapes with my camera
		</p>

		<div class="flex mb-6 w-full">
			<ul class="mx-auto text-left space-y-1">
				<li><a href="/publications">Visit Publications</a></li>
				<li><a href="/projects">Visit Projects <span class="text-xs">(WIP)</span></a></li>
				<li><a href="/sofortigramm/">Visit Photography</a></li>
			</ul>
		</div>

		<div class="flex flex-row gap-4 justify-center">
			<a
				href="https://github.com/ColdStormy"
				target="_blank"
				rel="noopener"
				class="px-2 py-1 text-white opacity-70 hover:opacity-100 transition flex items-center justify-center"
				aria-label="GitHub"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="w-4 h-4"
					><path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75 0 4.302 2.792 7.953 6.653 9.24.486.09.664-.211.664-.47 0-.232-.009-.846-.013-1.66-2.705.587-3.276-1.304-3.276-1.304-.442-1.123-1.08-1.422-1.08-1.422-.883-.604.067-.592.067-.592  .976.069 1.49 1.003 1.49 1.003.868 1.488 2.277 1.059 2.834.81.088-.629.34-1.06.618-1.304-2.16-.246-4.432-1.08-4.432-4.807 0-1.062.38-1.93 1.003-2.61-.101-.247-.435-1.24.096-2.586 0 0 .816-.262 2.676 1.001A9.36 9.36 0 0 1 12 6.844c.827.004 1.66.112 2.437.329 1.86-1.263 2.675-1.001 2.675-1.001.532 1.346.198 2.339.098 2.586.624.68 1.002 1.548 1.002 2.61 0 3.735-2.274 4.558-4.44 4.8.35.302.66.897.66 1.808 0 1.305-.012 2.36-.012 2.682 0 .26.176.563.67.468C18.96 19.95 21.75 16.302 21.75 12c0-5.385-4.365-9.75-9.75-9.75z"
					/></svg
				>
			</a>
			<a
				href="https://linkedin.com/in/jannistb/"
				target="_blank"
				rel="noopener"
				class="px-2 py-1 text-white opacity-70 hover:opacity-100 transition flex items-center justify-center"
				aria-label="LinkedIn"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="currentColor"
					viewBox="0 0 24 24"
					class="w-4 h-4"
					><path
						d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-10h3v10zm-1.5-11.268c-.966 0-1.75-.784-1.75-1.75s.784-1.75 1.75-1.75 1.75.784 1.75 1.75-.784 1.75-1.75 1.75zm13.5 11.268h-3v-5.604c0-1.337-.025-3.063-1.868-3.063-1.868 0-2.154 1.459-2.154 2.967v5.7h-3v-10h2.881v1.367h.041c.401-.761 1.379-1.563 2.838-1.563 3.036 0 3.6 2.001 3.6 4.599v5.597z"
					/></svg
				>
			</a>
			<a
				href="mailto:contact@j.bellok.de"
				class="px-2 py-1 text-white opacity-70 hover:opacity-100 transition flex items-center justify-center"
				aria-label="Email"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="w-5 h-5"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M3 8.5v7A2.5 2.5 0 0 0 5.5 18h13a2.5 2.5 0 0 0 2.5-2.5v-7A2.5 2.5 0 0 0 18.5 6h-13A2.5 2.5 0 0 0 3 8.5z"
					/>
					<path stroke-linecap="round" stroke-linejoin="round" d="M21 7.5l-9 6.5-9-6.5" />
				</svg>
			</a>
		</div>
		<div class="relative bottom-0 mt-50 mb-10 text-xs">&copy; 2025 Jannis Bellok</div>
	</div>
</section>

<style lang="scss">
	button {
		cursor: pointer;
	}

	a:hover {
		// text-shadow: 0 0 2px rgba(255, 255, 255, 0.3);
		color: rgba(153, 175, 255, 0.8);
	}
</style>
