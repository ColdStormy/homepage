<script>
	let scrollY = $state(0);

	const showScrollTop = $derived(scrollY > 300);

	function scrollToTop() {
		window.scrollTo({
			top: 0,
			behavior: 'smooth'
		});
	}
</script>

<svelte:window bind:scrollY />

{#if showScrollTop}
	<button
		onclick={scrollToTop}
		class="fixed bottom-8 right-8 bg-sky-600 hover:bg-sky-700 text-white p-3 rounded-full shadow-lg transition-all duration-300 ease-in-out hover:scale-110 z-50"
		aria-label="Scroll to top"
	>
		<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
			<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
		</svg>
	</button>
{/if}