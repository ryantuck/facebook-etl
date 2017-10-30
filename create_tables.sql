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

    user_id             text,
    post_id             text,
    reaction_type       text,

    primary key (user_id, post_id)
);

