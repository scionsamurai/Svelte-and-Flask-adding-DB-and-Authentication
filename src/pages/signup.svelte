<script>
    export let extraData;
    console.log(extraData);
    let current_user = extraData['current_user'];
    let test = extraData['test'];
    
</script>

<main class="index">
    <div class="banner">
        <h1>Signup</h1>
        <h3>Hello {current_user}!</h3>
        <span class="banner__right">
            <a href="/">
                <h5 class="home_button">Home</h5>
            </a>
            <a href="/login">
                <h5 class="login_button">Login</h5>
            </a>
            <a href="/signup">
                <h5 class="signup_button">Signup</h5>
            </a>
        </span>
    </div>
    {test}
</main>

