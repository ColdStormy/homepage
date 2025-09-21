<script>
	const publications = [
		{
			title: 'Evaluating Time Series Database Management Systems for Insurance Company',
			authors: 'A. Koschel, I. Astrova, S. -T. Alsleben, J. Bellok, N. Meyer and S. Meyer',
			venue:
				'13th International Conference on Information, Intelligence, Systems & Applications (IISA)',
			year: 2022,
			doi: '10.1109/IISA56318.2022.9904360',
			pages: '1-6',
			url: 'https://ieeexplore.ieee.org/document/9904360',
			urlName: 'IEEE Explore'
		},
		{
			title: 'Kombinierte Simulation logistikrelevanter Verkehrszusammenhänge',
			authors: 'Pump R, Baumann M, Bellok JT, Ahlers V, Koschel A',
			venue:
				'In Wittmann J (ed.) Simulation in Umwelt- und Geowissenschaften. Workshop Kassel 2019',
			year: 2019,
			ISBN: '978-3-8440-6981-5 (publisher)',
			url: 'https://www.shaker.de/de/content/catalogue/index.asp?lang=de&ID=8&ISBN=978-3-8440-6981-5',
			urlName: 'Shaker Verlag',
			pages: 'AM 171: 55–66',
			file: 'files/sug_2019.pdf'
		}
	];
</script>

<section
	class="min-h-screen py-16 px-4 bg-gradient-to-b from-slate-50 to-white font-sans text-slate-600"
>
	<div class="max-w-4xl mx-auto">
		<h1 class="text-3xl sm:text-4xl font-semibold mb-2">Publications</h1>
		<br />
		<ul class="space-y-4">
			{#each publications as pub}
				<li class="mb-5">
					{pub.authors}, <i>"{pub.title}"</i>, {pub.venue}, {pub.year}, {pub.pages},
					{#if pub.doi}
						doi: {pub.doi}
					{:else if pub.ISBN}
						ISBN: {pub.ISBN}
					{/if}
					<br />
					<a href={pub.url} class="text-sky-700">{pub.urlName}</a>
					<br />
					{#if pub.file}
						<a href={pub.file} class="text-sky-700">PDF eprint</a>
					{/if}
				</li>
			{/each}
		</ul>
		<br />
		<br />
		<a href="/" class="text-sky-700 flex items-center gap-1">
			<span aria-hidden="true">←</span> Back to Home
		</a>
	</div>
</section>
