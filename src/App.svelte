<script>
	
	let pages = {
		"index": "",
		"create": "",
		"login": "",
		"signup": "",
	}
	
	export let page;
	export let extraData;

	switch (page) {
		case 'index':
			import('./pages/index.svelte')
			.then(module => module.default)
			.then(Foo => pages[page] = Foo)
			.catch(err => console.error(err));
			break;
		case 'create':
			import('./pages/create.svelte')
			.then(module => module.default)
			.then(Foo => pages[page] = Foo)
			.catch(err => console.error(err));
			break;
		case 'login':
			import('./pages/login.svelte')
			.then(module => module.default)
			.then(Foo => pages[page] = Foo)
			.catch(err => console.error(err));
			break
		case 'signup':
			import('./pages/signup.svelte')
			.then(module => module.default)
			.then(Foo => pages[page] = Foo)
			.catch(err => console.error(err));
			break;
		}
</script>

<main>
	<svelte:component this={pages[page]} {extraData} />
</main>