create table replace_word
(
    id         bigserial not null
        constraint replace_word_pkey
            primary key,
    keyword    text      not null
        constraint replace_word_keyword_key
            unique,
    replace_to text      not null
);

INSERT INTO replace_word (id, keyword, replace_to) VALUES (1, '中2', 'ちゅうに');
INSERT INTO replace_word (id, keyword, replace_to) VALUES (2, 'ｗ', 'わら');
INSERT INTO replace_word (id, keyword, replace_to) VALUES (3, 'w', 'わら');
INSERT INTO replace_word (id, keyword, replace_to) VALUES (4, '？', 'ふぁっ');
INSERT INTO replace_word (id, keyword, replace_to) VALUES (5, '！', 'んっ');
INSERT INTO replace_word (id, keyword, replace_to) VALUES (6, 'ω', 'きゃんたま');
