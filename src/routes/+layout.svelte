<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/fav-jtb.png';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{@render children?.()}
