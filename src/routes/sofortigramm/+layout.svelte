<script lang="ts">
	let { children } = $props();
</script>

<section
	class="relative flex flex-col items-center justify-center min-h-screen px-4"
>
	<div class="w-full absolute top-0 xl:w-2/3">
        <a href="/sofortigramm"><h1 class="text-4xl font-bold text-center mb-8 py-10">Sofortigramm</h1></a>

        
        {@render children()}

		
		<p class="text-sm text-gray-500 justify-center">
			© 2025 Jannis Bellok. All rights reserved.
		</p>
	</div>
</section>
