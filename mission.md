# Here is the plan for our app -

## Backend

- Read watch library and subfolders
- Create search parameters from:
    - Filename
    - Cover Image hash
    - Any present metadata
- Rename and move file to appropriate subfolder structure.
- Write to SQL database data for library display

## API
- access RPGGeek with search parameters
- Return search results priority as
    - System/Game name
    - Individual book name
- On select of book, connect with RPGgeek again for -
    - library details/cover images, link to page (and DriveThruRPG if needed)

## Settings (as JSON)
- Path to current library/also include watch directory?
- Path to export library
- library settings:
    - Filename structure
    - Folder structure
    - Categories

## Frontend
- Display all TBD

## db

Table *games*
    - gid # game ID
    - Name # Game name (D&D)
    - RPGGeek ID
    - System
    - Ruleset/version
    - Publisher
    - Year of release

Table *library*
    - gid -> join to games
    - bid #book id
    - type # setting, core rules, supplement, module, etc.
    - path # path on disk
    - image # title image


### How does the user do this?

1. Search for a game name
    - by doing this, the system will add the game to the database and create the Objects along with the full library.
2. List books for selection
    - the system should also do a search in the existing directory/prompt for file selection
3. Move/rename book into new folder

Note: Any files not matched, either manually or automatically, we should prompt to do a fuzzy search for the book on RPGGeek as well.


Functions: 

1. Add System
2. Add Book
3. Select System
    a. Select Book