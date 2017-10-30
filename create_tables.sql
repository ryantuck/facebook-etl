create table fb_page (

    id                  text,
    name                text,

    primary key (id)
);

create table fb_post (

    id                  text,
    created_time        timestamp,
    message             text,

    primary key (id)
);

create table fb_comment (

    id                  text,
    post_id             text,
    created_time        timestamp,
    user_id             text,
    message             text,

    primary key (id)
);

create table fb_reaction (

    id                  text,
    post_id             text,
    user_id             text,
    reaction_type       text,

    primary key (id)
);

