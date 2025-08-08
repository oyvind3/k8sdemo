# GitHub Codespaces ♥️ Flask

Welcome to your shiny new Codespace running Flask! We've got everything fired up and running for you to explore Flask.

You've got a blank canvas to work on from a git perspective as well. There's a single initial commit with the what you're seeing right now - where you go from here is up to you!

Everything you do here is contained within this one codespace. There is no repository on GitHub yet. If and when you’re ready you can click "Publish Branch" and we’ll create your repository and push up your project. If you were just exploring then and have no further need for this code then you can simply delete your codespace and it's gone forever.

To run this application:

```
flask --debug run
```

### Azure AD Authentication

This sample integrates with [MSAL for Python](https://github.com/AzureAD/microsoft-authentication-library-for-python) to support signing in with Azure Active Directory.

Set the following environment variables before running the app:

```
export AZURE_CLIENT_ID=<application_client_id>
export AZURE_CLIENT_SECRET=<application_client_secret>
# Optional: use a tenant-specific authority
# export AZURE_AUTHORITY="https://login.microsoftonline.com/<tenant_id>"
export FLASK_SECRET=<random string>
```

Start the app and visit `/login` to sign in or `/logout` to end the session.
