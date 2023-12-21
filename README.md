# RPGShelf (temporary name)

Have you collected *far* too many TTRPG rulebooks, supplements, modules, maps, tokens, errata, and more? Do they clutter up your hard drive?

Did you buy a Humble Bundle, or an Itch.io sale, and now you have a dozen (or more) vaguely labelled files in a folder?

The RPGshelf aims to be a way to clean this up and serve the files to you via a self-hosted solution accessible from anywhere, and share the files as needed to your players.

## But how do we do this?

Simple - the plan is to start with tagging and organizing your library. We use rpggeek.com for the API, as there is nowhere else that provides access.

    - tell us where your library is located and optionally where you want your library to be.
    - add a game to your library. We'll create a folder for you.
    - find the book on your hard drive, and tell us which book in the system it is.
    - we will move the file (or copy if you would prefer) to the folder, into a subfolder if desired (for "Core," "Module," "Supplement," etc. as you can define), rename it to something standardized, and list the file in an SQLite database to include more data.

## Where are you getting this data?

See, most supplements don't have ISBNs, or a bunch of stuff comes off of Itch.io as self-published material. You wouldn't find them on Amazon, and you might find them on DriveThruRPG.

And yet, RPGGeek seems to be the *only* open api that can provide access to all the assets for tabletop games, and their database seems pretty damn *exhaustive.* They seem to be good folks, so go give them a gander.

## This is fantastic, where did you get the idea?

The idea similar to the myriad other media organizers, particularly taking inspiration from the various comic book libraries such as Komga, Kavita, etc., but with tagging and organization for TTRPGs specifically.

The basic idea is inspired by ComicTagger, a useful tagging tool that pulls data from an external source and writes the CBR metadata.

PDFs don't have much metadata, though, so we'll use an SQLite database to provide extended data for later access.

## This app doesn't look like it does all that yet.

Well, it doesn't. This is still in early stages, and I'm learning Python for the backend as I go.

I plan to eventually:
    - include a lovely JavaScript frontend.
    - add a file reader
    - add custom notes and campaigns
    - hopefully set up integration with FoundryVTT
    - the ability to insert/indicate errata on the appropriate asset/page.
    - and much, much more.

But see, this is one of my early projects, and as I say: my ambition usually outweights my abilities. Wish me luck, though!

## I mean, you're a splendid coder and your idea is great. Can I contribute?

Absolutely you can. I am [OMGtheGreenRanger](https://github.com/omgthegreenranger), and the repository is [here](https://github.com/omgthegreenranger/rpgshelf). If this whole thing gets some eyes and people are interested, I'll absolutely need some help to get better.