<svelte:head>
	<title>login - OurSite</title>
</svelte:head>

<main>
    <form method="post">
        <h1 class="header">Our App Name</h1>
        <h5 class="header2">Log into Account</h5>
        <div class="form-inputs">
            <div class="form__group field">
                <input type="text" class="form__field" placeholder="Name" name="username" id='username' required />
                <label for="username" class="form__label">Username</label>
            </div>
            <div class="form__group field">
                <input type="password" class="form__field" placeholder="Password" name="password" id='password' required />
                <label for="password" class="form__label">Password</label>
            </div>
            <div class="forgot-password">
                <a href="/#">Forgot Password?</a>
            </div>

            <button id="btn" class="signin"  type="submit">Sign In</button>
        </div>
    </form>
</main>
