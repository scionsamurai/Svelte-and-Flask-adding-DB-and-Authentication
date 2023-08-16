import App from './App.svelte';

const target_element = document.getElementById("svelte");
const data_element = document.getElementById("data");
const app = new App({
	target: target_element,
	props: {
		page: target_element.getAttribute("data-page"),
		extraData: data_element !== null && data_element.innerHTML ? JSON.parse(data_element.innerHTML) : null
	}
});

export default app;