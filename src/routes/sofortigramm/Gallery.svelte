<script lang="ts">
	import { onMount } from 'svelte';

	const TOTAL_PHOTOS = 55;
	const PHOTOS_PER_BATCH = 12;
	const SCROLL_THRESHOLD = 300; // Load more when 300px from bottom

	// Generate all photo metadata but don't add to visible list yet
	const generatePhoto = (i: number) => {
		const height = Math.floor(Math.random() * 200) + 200; // Random height between 200 and 400
		const width = Math.floor(Math.random() * 200) + 300; // Random width between 300 and 500
		const aspectRatio = width / height;
		
		return {
			src: `https://picsum.photos/seed/coldstormy${i}/${width}/${height}`,
			alt: `Sample photo ${i}`,
			title: [
				'Beautiful Landscape',
				'City Architecture',
				'Nature Photography',
				'Street Photography',
				'Portrait Session',
				'Abstract Art'
			][(i - 1) % 6],
			aspectRatio
		};
	};

	interface Photo {
		src: string;
		alt: string;
		title: string;
		aspectRatio: number;
	}

	let visiblePhotos: Photo[] = $state([]);
	let loadedCount = $state(0);
	let columns: Photo[][] = $state([]);
	let loading = $state(false);
	
	const loadMorePhotos = () => {
		if (loading || loadedCount >= TOTAL_PHOTOS) return;
		
		loading = true;
		const nextBatch = [];
		const batchSize = Math.min(PHOTOS_PER_BATCH, TOTAL_PHOTOS - loadedCount);
		
		for (let i = 0; i < batchSize; i++) {
			nextBatch.push(generatePhoto(loadedCount + i + 1));
		}
		
		visiblePhotos = [...visiblePhotos, ...nextBatch];
		loadedCount += batchSize;
		loading = false;
		redistributePhotos();
	};

	const redistributePhotos = () => {
		let innerWidth = window.innerWidth;
		const numColumns = innerWidth < 640 ? 1 : innerWidth < 768 ? 2 : innerWidth < 1024 ? 3 : 4;
		columns = Array.from({ length: numColumns }, () => []);
		visiblePhotos.forEach((photo, idx) => {
			columns[idx % numColumns].push(photo);
		});
	};
	
	const handleResize = () => {
		redistributePhotos();
    };

	const handleScroll = () => {
		const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
		const windowHeight = window.innerHeight;
		const documentHeight = document.documentElement.scrollHeight;
		
		if (scrollTop + windowHeight >= documentHeight - SCROLL_THRESHOLD) {
			loadMorePhotos();
		}
	};

	onMount(() => {
        window.addEventListener('resize', handleResize);
        window.addEventListener('scroll', handleScroll);
        
        // Load initial batch of photos
        loadMorePhotos();

        return () => {
			window.removeEventListener('resize', handleResize);
			window.removeEventListener('scroll', handleScroll);
		};
    })
</script>

{#each columns as column}
    <div class="flex flex-col gap-6 flex-1">
        {#each column as photo}
            <div 
                class="bg-white transition-transform overflow-hidden hover:cursor-pointer w-full relative photo-container"
                style="aspect-ratio: {photo.aspectRatio};"
            >
                <img
                    src={photo.src}
                    alt={photo.alt}
                    class="w-full h-full object-cover transition-transform duration-200 ease-out hover:scale-110"
                    loading="lazy"
                    decoding="async"
                />
                <div class="w-full h-full relative placeholder animate-pulse"></div>
            </div>
        {/each}
    </div>
{/each}
            

<style>
	.photo-container::after {
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		box-shadow: inset 0px 0px 100px 22px rgba(0, 0, 0, 0.4);
		pointer-events: none;
		z-index: 1;
	}
</style>
