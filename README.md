# [CHARLES GEMINI APPAREL](https://charles-gemini-apparel-6a23d410a6ee.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/boderg/charles-gemini-apparel)](https://github.com/boderg/charles-gemini-apparel/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/boderg/charles-gemini-apparel)](https://github.com/boderg/charles-gemini-apparel/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/boderg/charles-gemini-apparel)](https://github.com/boderg/charles-gemini-apparel)

Charles Gemini Apparel is an online clothing retail store specialising in T-Shirts and Hooded Tops with custom design prints.

Charles Gemini Apparel was designed from the ground up by Simon Boylan for their Code Institute Milestome Project 4 and is a fully functioning site utilising the Stripe API for payments and GMail for sending confirmation emails.

Users of the Charles Gemini site are able to create user accounts where they can save their details and orders for future use and view their past orders.

Users are able to send messages to the admin of the Charles Gemini Apparel site through a contact form and users can also sign up with their email to receive newsletters.

*Below is a mockup of the deployed Charles Gemini Apparel site.*

![screenshot](documentation/mockup.png)
source: [amiresponsive](https://ui.dev/amiresponsive?url=https://charles-gemini-apparel-6a23d410a6ee.herokuapp.com)

## UX

The process for the design of the Charles Gemini Apparel site started as a collection of user stories outlining the purpose and use for the site.

A rough idea was drawn up on paper that would outline the database structure for the Charles Gemini Apparel site.

Wireframes were then created using [Balsamiq](https://balsamiq.com/) to get a general feel for how the site would look.

The Charles Gemini Apparel site was then built using Django, Python, HTML, Bootstrap, CSS,and JavaScript.

### Colour Scheme

The colour scheme chosen for the site was one that would be comfortable on the eye but also inviting, pleasing to navigate and easy to read.

*Below is a colour palette of the colours chosen to fit the scheme.*

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

### Typography

Only one font was chosen for the Charles Gemini Apparel site.

[Cuprum](https://fonts.google.com/?query=cuprum)

- This [Google](https://fonts.google.com/) font was chosen because it is the font used in the Logo, has a clean and modern style and scales nicely for the purpose of the site.

Two sources were used for the icons acros the Charles Gemini Apparel site.

[UXWing](https://uxwing.com/)

- These icons were used across the Charles Gemini Apparel site as they add a certain style that compliments the site along with a splash of colour. They are also available as SVG's which allowed for easy colour changing to match the site as all black icons were re-coloured to `#373737` to match the font and the magnifying glass re-coloured from blue to `#93ff00`.

[Font Awesome](https://fontawesome.com/)

- A few Font Awesome icons were used, namely for the plus and minus buttons and the left arrow on some back buttons. These were used as there were either no UXWing equivalents or the UXWing equivqlent did not match the site aesthetic.

## User Stories

### New Site Users

- As a new site user, I would like to be able to easily browse through all the t-shirts and hooded tops on the website, filtered by category, so that I can quickly find something that interests me.
- As a new site user, I would like to be able to search for t-shirts and hooded tops by keyword, so that I can see if you have what I'm looking for.
- As a new site user, I would like to see a detailed product page with clear, high-resolution images, so that I can make a more informed choice.
- As a new site user, I would like to be able to see the shirt or hoodie in different colors, so that I can ensure I choose the right one.
- As a new site user, I would like to be able to see a size chart with clear measurements, so that I can ensure a proper fit.
- As a new site user, I would like to be able to easily add items to my cart, so that I can securely purchase them.
- As a new site user, I would like to be able to clearly see the total cost of my order, including any taxes and shipping fees, so that I can be better informed before finalizing the purchase.

### Returning Site Users

- As a returning site user, I would like to be able to create an account, so that I can save my shipping information and track my order history.
- As a returning site user, I would like to be able to sign up for an email list to receive notifications, so that I can stay informed about new arrivals, promotions, and exclusive offers.
- As a returning site user, I would like to have a way to contact the site admin, so that I can get resolutions to issues I may have with my account.
- As a returning site user, I would like to contact the company, so that I can pass on suggestions or compliments.

### Site Admin

- As a site administrator, I should be able to have an easy site access method, so that I can add new t-shirt and hooded top designs to the website, including uploading high-quality images, descriptions, and pricing information.
- As a site administrator, I should be able to create and manage product categories and collections, so that I can organize the website for easy browsing.
- As a site administrator, I should be able to edit existing product information, such as descriptions, pricing, and images, so that I can keep the website content accurate and up-to-date.
- As a site administrator, I should be able to create and manage discounts, so that I can attract new customers.
- As a site administrator, I should be able to view and manage customer contacts, so that I can send the relevant newsletter or contact reply.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.

<details>
<summary>Please click to view the Mobile wireframes for Charles Gemini Apparel</summary>
<br>

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/wireframes/mobile/home.png) | ![screenshot](documentation/wireframes/tablet/home.png) | ![screenshot](documentation/wireframes/desktop/home.png) |
| All Designs (*New Designs, Tees and Hoodies follow the same format.*) | ![screenshot](documentation/wireframes/mobile/all_designs.png) | ![screenshot](documentation/wireframes/tablet/all_designs.png) | ![screenshot](documentation/wireframes/desktop/all_designs.png) |
| Garment | ![screenshot](documentation/wireframes/mobile/garment.png) | ![screenshot](documentation/wireframes/tablet/garment.png) | ![screenshot](documentation/wireframes/desktop/garment.png) |
| Empty Bag (*404 and 500 pages use the same format.*) | ![screenshot](documentation/wireframes/mobile/empty_bag.png) | ![screenshot](documentation/wireframes/tablet/empty_bag.png) | ![screenshot](documentation/wireframes/desktop/empty_bag.png)|
| Bag | ![screenshot](documentation/wireframes/mobile/bag.png) | ![screenshot](documentation/wireframes/tablet/bag.png) | ![screenshot](documentation/wireframes/desktop/bag.png) |
| Checkout | ![screenshot](documentation/wireframes/mobile/checkout.png) | ![screenshot](documentation/wireframes/tablet/checkout.png) | ![screenshot](documentation/wireframes/desktop/checkout.png) |
| Checkout Success | ![screenshot](documentation/wireframes/mobile/checkout_success.png) | ![screenshot](documentation/wireframes/tablet/checkout_success.png) | ![screenshot](documentation/wireframes/desktop/checkout_success.png) |
| Profile | ![screenshot](documentation/wireframes/mobile/profile.png) | ![screenshot](documentation/wireframes/tablet/profile.png) | ![screenshot](documentation/wireframes/desktop/profile.png) |
| Admin Panel | ![screenshot](documentation/wireframes/mobile/admin_panel.png) | ![screenshot](documentation/wireframes/tablet/admin_panel.png) | ![screenshot](documentation/wireframes/desktop/admin_panel.png)  |
| Add Garment | ![screenshot](documentation/wireframes/mobile/add_garment.png) | ![screenshot](documentation/wireframes/tablet/add_garment.png) | ![screenshot](documentation/wireframes/desktop/add_garment.png) |
| Edit Garment (*Pre-populated version of add garment.*) | ![screenshot](documentation/wireframes/mobile/edit_garment.png) | ![screenshot](documentation/wireframes/tablet/edit_garment.png) | ![screenshot](documentation/wireframes/desktop/edit_garment.png) |
| Selection Page (*The same format is used for all selection pages (garment, category, colour, size, contact and subscriber).*) | ![screenshot](documentation/wireframes/mobile/selection_page.png) | ![screenshot](documentation/wireframes/tablet/selection_page.png) | ![screenshot](documentation/wireframes/desktop/selection_page.png) |
| Add / Edit Item (*The same format is used for the category, colour, and size pages. Edit pages are pre-populated.*) | ![screenshot](documentation/wireframes/mobile/add-edit_item.png) | ![screenshot](documentation/wireframes/tablet/add-edit_item.png) | ![screenshot](documentation/wireframes/desktop/add-edit_item.png) |
| About Modal | ![screenshot](documentation/wireframes/mobile/about.png) | ![screenshot](documentation/wireframes/tablet/about.png) | ![screenshot](documentation/wireframes/desktop/about.png) |
| Size Guide Modal | ![screenshot](documentation/wireframes/mobile/size_guide.png) |![screenshot](documentation/wireframes/tablet/size_guide.png)  | ![screenshot](documentation/wireframes/desktop/size_guide.png) |

</details>

## Features

### Existing Features

<details>
<summary>Please click to view the Mobile wireframes for Charles Gemini Apparel</summary>
<br>

| Page | Section | Feature | Description | Screenshot |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Top Nav| | | |
| | | Charles Gemini Apparel Logo | This is the brand log and also doubles as the Home page button. | ![screenshot](documentation/features/charles_gemini_logo.png) |
| | | Shop Now Button| This is the main navigation for the site. | ![screenshot](documentation/features/shop_now_button.png) |
| | | Search Bar | This enables the user to search for products that are on the site. | ![screenshot](documentation/features/search_bar.png) |
| | | Bottom Nav | | |
| | | Shopping Bag Icon | This is set up as a button and takes the user to the shopping bag. It also displays as a counter to inform of the quantity of items in the bag. | ![screenshot](documentation/features/bag_button.png) ![screenshot](documentation/features/bag_counter.png) |
| | | Login / Logout Icon | This is set up as a button and takes the user to the login or logout page dependant on whether the user is logged in or not. It is a dynamic button and switches between icons accordingly. | ![screenshot](documentation/features/login_button.png) ![screenshot](documentation/features/logout_button.png) |
| | Main | | | |
| | | Information Banner | This s a display tool that displays fixed messages and/or promotions, such as the free delivery message or the bag total. | ![screenshot](documentation/features/banner_1.png) ![screenshot](documentation/features/banner_2.png) |
| | | Page Link Cards (Tees, New Designs and Hoodies) | These act as descriptors for the site and double as navigation to the Tees, New Designs and Hoodies pages respecively. the middle one is also a carousel rotating between its descriptor image and the brand logo. | ![screenshot](documentation/features/page_links.png) |
| | Footer | | | |
| | | Newsletter signup Button | This button navigates the user to a simple signup form where they can submit their email to receive email newsletters. | ![screenshot](documentation/features/newsletter_signup_button.png) |
| | | Admin Panel Button | This button navigates authorised users to the sites front end admin panel. This button is only visible to authorised logged in users. | ![screenshot](documentation/features/admin_panel_button.png) |
| | | GitHub Icon | This is set up as a button that opens the site creators GitHub repository on a separate page. | ![screenshot](documentation/features/github_icon.png) |
| | | Social Media Icons | These icons are set up as buttons that open the associated social media sites on a new tab. These would ideally link to the social media pages of Charles Gemini Apparel. | ![screenshot](documentation/features/social_icons.png) |
| All Designs, New Designs, Tees and Hoodies | | | | |
| | Main | | | |
| | |Garment Cards | These show a brief outline of the products along with price and and image. The image of the card is a link that navigates the user to the individual garment page. | ![screenshot](documentation/features/garment_images.png) |
| Garment | | | | |
| | Main | | | |
| | | Garment Card | This displays all the information related to an individual garment, such as available sizes and colours, description, images and price. | ![screenshot](documentation/features/garment_card.png) |
| | Garment Card Items | | | |
| | | Image Carousel | This displays the item in all its available colours and rotates through each colour in turn. The images can be stopped and rotated manually or left to rotate automatically. | ![screenshot](documentation/features/image_carousel.png) |
| | | Number Selector | This is set up to allow users to adjust the quantity of the product they want to purchase. It will not allow numbers outside of the range 1-99 to be used. the plus and minus buttons change to a darker grey and stop changing the number counter when they have reached the range limit. | ![screenshot](documentation/features/number_selector.png) |
| | | Size Selector | This opens a dropdown list of selectable sizes and is to allow the user to select a size that suits them. | ![screenshot](documentation/features/size_selector.png) |
| | | Size Guide Button | This is set to open a modal that contains an informative size guide for the user to make an informed choice about the sizing of the item that they are interested in. | ![screenshot](documentation/features/size_guide_button.png) |
| | | Colour Selector | This opens a dropdown list of selectable colours the item is available in and is to allow the user to select a colour that suits them. | ![screenshot](documentation/features/colour_selector.png) |
| | | Add to Bag Button | This is to allow the user to add their current item selection to the shopping bag. | ![screenshot](documentation/features/add_to_bag.png) |
| | | All Designs Button | This is to allow users to navigate away from the item page without using the browsers back arrow nd without saving the current selection if any has been made. this navigates to the all designs page. | ![screenshot](documentation/features/all_designs.png) |
| | | Available Colours | This displays colour swatches of the colours that the item is available in. | ![screenshot](documentation/features/colour_swatches.png) |
| Shopping Bag | | | | |
| | Bag Table | | | |
| | | Number Selector | This is set up to allow users to change the quantity of the selcted item. It will not allow numbers outside of the range 1-99 to be used. the plus and minus buttons change to a darker grey and stop changing the number counter when they have reached the range limit. | ![screenshot](documentation/features/number_selector1.png) |
| | | Size Selector | This opens a dropdown list of selectable sizes and is to allow the user to changethe selected size. | ![screenshot](documentation/features/size_selector1.png) |
| | | Colour Selector | This opens a dropdown list of selectable colours the item is available in and is to allow the user to change the selected colour. | ![screenshot](documentation/features/colour_selector1.png) |
| | | Update Button | This updates the shopping bag with newly changed colour, size or quantity if the user has changed the selected items in the bag. | ![screenshot](documentation/features/update_button.png) |
| | | Remove Button | This allows the user to remove any item from the bag should they decide not to purchase or if they have added by mistake. | ![screenshot](documentation/features/remove_button.png) |
| | | Continue Shopping Button | This allows the user to go back into the shop should they wish to browse and/or add other items prior to purchase. | ![screenshot](documentation/features/continue_shopping_button.png) |
| | | Secure Checkout Button | This navigates the user to the payment window and puts the items from the bag into the checkout. | ![screenshot](documentation/features/secure_checkout_button.png) |
| Checkout | | | | |
| | Order Summary | | | |
| | | Order Summary | This displays the order details to the user as a final sumamry before purchase. | ![screenshot](documentation/features/order_sumamry.png) |
| | | Change Your Order Button | This allows the user to go back to the bag and make changes to the order before purchase. this is the final get out of the sale method before final purchase. | ![screenshot](documentation/features/change_your_order_button.png) |
| | Checkout Form | | | |
| | | Contact Details | this is where the user adds their contact details for the order. | ![screenshot](documentation/features/contact_details.png) |
| | | Billing and Delivery Details | This is where the user adds their address for billing abd delivery purposes. | ![screenshot](documentation/features/billing_details.png) |
| | | Create Account Link | This allows a non-registered user to create an account and save the details for quicker future purchases. | ![screenshot](documentation/features/create_account_link.png) |
| | | Login Link | This allows a registered user to login and retrieve their details for the purchase. | ![screenshot](documentation/features/login_link.png) |
| | | Card Payment Input | this allows the user to safely and securely use a credit / debit card for payment. | ![screenshot](documentation/features/card_details.png) |
| | | Complete Order Button | This processes the payment and is an irreversible process once clicked. The users card will then be charged with the billed amount. | ![screenshot](documentation/features/complete_order_button.png) |
| Checkout Success | | | | |
| | Order Summary | | | |
| | | Thank You | This displays thank you message with order number, date of order and confirmation email notification. | ![screenshot](documentation/features/thank_you.png) |
| | | Your Order | This displays a confirmation of the ordered products, prices and totals. | ![screenshot](documentation/features/order_summary1.png) |
| | | Delivery Info and Billing Info | This displays a confirmation of the address supplied for billing and delivery. | ![screenshot](documentation/features/billing_details1.png) |
| | | Continue Shopping Button | This allows the user to go back into the shop after a purchase and is worder to entice users to make further purchases. | ![screenshot](documentation/features/continue_shopping1.png) |
| My Profile | | | | |
| | Default Delivery Information | | | |
| | | Update Information Form and Button | This allows users to update their default delivery address when they have completed the form that the button is attached to. | ![screenshot](documentation/features/update_info.png) |
| | Order History | | | |
| | | Order Links | These are previous order numbers that have been formatted to act as links that open the associated order to allow users to view their previous orders. | ![screenshot](documentation/features/order_link.png) |
| Admin Panel | | | | |
| | Main | | | |
| | | Admin Panel | This panel houses front end access buttons for the database admin of the site. These buttons access the front end pages that allow the admin of the site to add, remove and edit items in the store. | ![screenshot](documentation/features/admin_panel.png) |
| Add and Edit Garment | | | | |
| | Main | | | |
| | | Add and Edit Garment Forms | These forms allow the site admin to add and edit garments. The add garment form opens empty while the edit garments form opens pre-populated with the selected garments details. | ![screenshot](documentation/features/add_garment_form.png) |
| | | Add and Edit Garment Buttons | This submits the completed form to the database saving the new item or changed item and redirects the user to the items page. | ![screenshot](documentation/features/add_garment_button.png) ![screenshot](documentation/features/edit_garment_button.png) |
| | | Back to Garments Button | Returns the site admin to the all designs page without saving the changed or newly added garment.  | ![screenshot](documentation/features/back_to_garments_button.png) |
| Add and Edit Category, Colour and Size | | | | |
| | Main | | | |
| | | Add and Edit Category Forms | These forms allow the site admin to add new or edit existing categories dependant on the selected. The edit form is a pre-populated version of the add form. | ![screenshot](documentation/features/add_category_form.png) |
| | | Add and Edit Colour Forms | These forms allow the site admin to add new or edit existing colours dependant on the selected. The edit form is a pre-populated version of the add form. | ![screenshot](documentation/features/add_colour_form.png) |
| | | Add and Edit Size Forms | These forms allow the site admin to add new or edit existing sizes dependant on the selected. The edit form is a pre-populated version of the add form. | ![screenshot](documentation/features/add_size_form.png) |
| Garment, Category, Colour and Size Selection | | | | |
| | Main | | | |
| | | Listed Items from garments, categories, colour and sizes | This is a listed display of the items that are available to edit or delete and is accessed from one of the main edit buttons on the admin panel. | ![screenshot](documentation/features/listed_item.png) |
| | | Contact List and Subscribers | This is the same as the listed item but does not have the edit function. | ![screenshot](documentation/features/contact_item.png) |
| | | Edit Button | This allows the admin access to the edit form for item that is selected from the listed items. | ![screenshot](documentation/features/blue_edit_category_button.png) ![screenshot](documentation/features/blue_edit_colour_button.png) ![screenshot](documentation/features/blue_edit_size_button.png) ![screenshot](documentation/features/blue_edit_garment_button.png) |
| | | Delete Button | This allows the admin access to the delete function for item that is selected from the listed items, contact list and subscribers. | ![screenshot](documentation/features/red_delete_category_button.png) ![screenshot](documentation/features/red_delete_colour_button.png) ![screenshot](documentation/features/red_delete_size_button.png) ![screenshot](documentation/features/red_delete_garment_button.png) ![screenshot](documentation/features/red_delete_contact.png) ![screenshot](documentation/features/red_delete_subscriber.png) |
| | Modals | | | |
| | | Delete Modal | This accessed by the site admin when any of the admin delete buttons are clicked. This is to double confirm that the user wants to delete the item. | ![screenshot](documentation/features/delete_modal.png) |
| | | About Modal | This modal is accessed by clicking the about link in main site navigation and displays information about the brand. | ![screenshot](documentation/features/about_modal.png) |
| | | Size Guide Modal | This is accessed by clicking any of the size guide links and displays sizing information about the products. | ![screenshot](documentation/features/size_guide_modal.png) |

</details>

### Future Features

Some future features that would be good to add to the site in the future:

Payment Methods

- Different types of payment methods e.g. Paypal, Klarna, etc.

Reveiw System

- An ability for users to review the products for others to make informed choices.

Rating system

- Similar to the review system but with a number or star system.

Email return system

- Somewhere admin and staff can return an email to the customer without using an external system.

Automated Newsletters

- Automate newsletters to send to the subscribers when new newsletters are created.

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![VSCode](https://img.shields.io/badge/VSCode-grey?logo=visualstudiocode&logoColor=007ACC)](https://code.visualstudio.com) used as my local IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![jQuery](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.
- [![Stripe](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) used for online secure payments of ecommerce products/services.
- [![Gmail API](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) used for sending emails in my application.
- [![AWS S3](https://img.shields.io/badge/AWS_S3-grey?logo=amazons3&logoColor=569A31)](https://aws.amazon.com/s3) used for online static file storage.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.
- [![Canva](https://img.shields.io/badge/Canva-grey?logo=canva&logoColor=00C4CC)](https://www.canva.com/p/canvawireframes) used for creating the brand logo and some garment designs.
- [![Krita](https://img.shields.io/badge/Krita-grey?logo=Krita
)](https://krita.org/en/) used for creating garment designs.
- [![Inkscape](https://img.shields.io/badge/Inkscape-grey?logo=inkscape
)](https://inkscape.org/) used for re-colouring the uxwing svg icons. 
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.

## Database Design

Charles Gemini Apparel uses a relational database.

It was built during development using Django's built in SQLite3 database. For deployment all the built models were migrated over to a PostgreSQL database hosted by Code Institute.

Below is a Database diagram that was built during the development of the Charles Gemini Apparel site,

![screenshot](documentation/erd/cga_erd1.png)
source: [dbdiagram.io](https://www.dbdiagram.io/)

and a more comprehensive diagram created after deployment and testing.

![screenshot](documentation/erd/cga_erd.png)
source: [pygraphviz](https://pygraphviz.github.io/documentation/stable/install.html)

## Testing

>[!NOTE]
>
>For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://charles-gemini-apparel-6a23d410a6ee.herokuapp.com).

### PostgreSQL Database

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net).

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Signed-in to the CI LMS using my email address.
- An email was sent to me with my new Postgres Database.

> [!CAUTION]  
>
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method
> if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

    ```shell
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
- Policy Type: **S3 Bucket Policy**
- Effect: **Allow**
- Principal: `*`
- Actions: **GetObject**
- Amazon Resource Name (ARN): **paste-your-ARN-here**
- Click **Add Statement**
- Click **Generate Policy**
- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

    ```shell
    {
        "Id": "Policy1234567890",
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "Stmt1234567890",
                "Action": [
                    "s3:GetObject"
                ],
                "Effect": "Allow",
                "Resource": "arn:aws:s3:::your-bucket-name/*"
                "Principal": "*",
            }
        ]
    }
    ```

- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
  - If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
  - Suggested Name: `group-charles-gemini-apparel` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
  - Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
  - You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

    ```shell
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": [
                    "arn:aws:s3:::your-bucket-name",
                    "arn:aws:s3:::your-bucket-name/*"
                ]
            }
        ]
    }
    ```

  - Click **Review Policy**.
  - Suggested Name: `policy-charles-gemini-apparel` (policy + the project name)
  - Provide a description:
  - "Access to S3 Bucket for charles-gemini-apparel static files."
  - Click **Create Policy**.
- From **User Groups**, click your "group-charles-gemini-apparel".
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-charles-gemini-apparel") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
  - Suggested Name: `user-charles-gemini-apparel` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-charles-gemini-apparel`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
  - **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
  - This contains the user's **Access key ID** and **Secret access key**.
  - `AWS_ACCESS_KEY_ID` = **Access key ID**
  - `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.
