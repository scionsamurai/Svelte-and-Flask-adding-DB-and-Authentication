<svelte:head>
	<title>signup - OurSite</title>
</svelte:head>

<main>
    <form method="post">
        <h1 class="header">Our App Name</h1>
        <h5 class="header2">Create an Account</h5>
        <div class="form-inputs">
            <div class="form__group field">
                <input type="text" class="form__field" placeholder="Name" name="username" id='username' required />
                <label for="username" class="form__label">Username</label>
            </div>
            <div class="form__group field">
                <input type="email" class="form__field" placeholder="Email" name="email" id='email' required />
                <label for="email" class="form__label">Email</label>
            </div>
            <div class="form__group field">
                <input type="password" class="form__field" placeholder="Password" name="password" id='password' required />
                <label for="password" class="form__label">Password</label>
            </div>
            <div class="form__group field">
                <input type="password" class="form__field" placeholder="Confirm Password" name="confirm_password" id='confirm_password' required />
                <label for="confirm_password" class="form__label">Confirm Password</label>
            </div>

            <button id="btn" class="signup" type="submit">Sign Up</button>
        </div>
    </form>
</main>
