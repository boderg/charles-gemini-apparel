# [CHARLES GEMINI APPAREL](https://charles-gemini-apparel-6a23d410a6ee.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/boderg/charles-gemini-apparel)](https://github.com/boderg/charles-gemini-apparel/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/boderg/charles-gemini-apparel)](https://github.com/boderg/charles-gemini-apparel/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/boderg/charles-gemini-apparel)](https://github.com/boderg/charles-gemini-apparel)

Charles Gemini Apparel is an online clothing retail store specialising in T-Shirts and Hooded Tops with custom design prints.

Charles Gemini Apparel was designed from the ground up by Simon Boylan for their Code Institute Milestome Project 4 and is a fully functioning site utilising the Stripe API for payments and GMail for sending confirmation emails.

Users of the Charles Gemini site are able to create user accounts where they can save their details and orders for future use and view their past orders.

Users are able to send messages to the admin of the Charles Gemini Apparel site through a contact form and users can also sign up with their email to receive newsletters.

Below is a mockup of the deployed Charles Gemini Apparel site.

![screenshot](documentation/mockup.png)
source: [amiresponsive](https://ui.dev/amiresponsive?url=https://charles-gemini-apparel-6a23d410a6ee.herokuapp.com)

## UX

The process for the design of the Charles Gemini Apparel site started as a collection of user stories outlining the purpose and use for the site.

A rough idea was drawn up on paper that would outline the database structure for the Charles Gemini Apparel site.

Wireframes were then created using [Balsamiq](https://balsamiq.com/) to get a general feel for how the site would look.

The Charles Gemini Apparel site was then built using Django, Python, HTML, Bootstrap, CSS,and JavaScript.

### Colour Scheme

The colour scheme chosen for the site was one that would be comfortable on the eye but also inviting, pleasing to navigate and easy to read.

Below is a colour palette of the colours chosen to fit the scheme.

![screenshot](documentation/colour_palette.png)
source: [coolors.co](https://coolors.co/93ff00-373737-fafafa-bcdcf5)

- `#93ff00` used for top navbar, footer and highlights.
- `#373737` used for text across the site on light backgrounds.
- `#fafafa` used for text on dark backgrounds and buttons.
- `#bcdcf5` used for main body background and image backgrounds.

Variations of these colours were worked to enable the softening of some of the colours with some opacity introduced for effect.

I've used CSS `:root` variables to easily update the global colour scheme, borders, shadows and font by changing only one value, instead of everywhere in the CSS file.

```CSS
:root {
    /** Fonts **/
    --main-font: 'Cuprum', sans-serif;

    /** Colours **/
    --body-background: rgb(188, 220, 245, 0.255);
    --body-background-translucent: rgba(188, 220, 245, 0.855);
    --background: rgb(250, 250, 250);
    --background-translucent: rgba(250, 250, 250, 0.75);
    --background-translucent-2: rgba(250, 250, 250, 0.5);
    --primary-colour: rgb(147, 255, 0);
    --primary-colour-translucent: rgba(147, 255, 0, 0.5);
    --primary-colour-translucent-2: rgba(147, 255, 0, 0.3);
    --primary-colour-translucent-3: rgba(147, 255, 0, 0.7);
    --secondary-colour: rgb(55, 55, 55);
    --secondary-colour-translucent: rgba(55, 55, 55, 0.5);
    --secondary-colour-translucent-2: rgba(55, 55, 55, 0.3);
    --warning-colour: rgb(249, 225, 84);
    --error-colour: rgb(200, 50, 50);
    --info-colour: rgb(64, 166, 206);
    --success-colour: rgb(147, 255, 0);

    /** Shadows **/
    --big-box-shadow: 1px 1px 10px rgb(55, 55, 55);
    --small-box-shadow: 1px 1px 5px rgb(55, 55, 55);
    --small-box-shadow-invert: 1px 1px 5px rgb(250, 250, 250);
    --big-inset-box-shadow: inset 1px 1px 5px rgb(55, 55, 55);
    --small-inset-box-shadow: inset 1px 1px 3px rgb(55, 55, 55);
    --text-shadow: 1px 1px 1px rgb(55, 55, 55);

    /** Borders **/
    --thin-border: 1px solid rgb(55, 55, 55);
    --border-radius: 3px;

    /** Other **/
    --transition-quick: all 0.2s ease-in-out;
}
```
