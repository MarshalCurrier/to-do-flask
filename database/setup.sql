
DROP TABLE IF EXISTS account_status CASCADE;
DROP TABLE IF EXISTS profiles CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;
DROP TABLE IF EXISTS task_status CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS roles CASCADE;

CREATE TABLE roles (
    roles_id    serial primary key,
    role_name    VARCHAR(24) not null
);

CREATE TABLE account_status (
    account_status_id    serial primary key,
    account_status_name    VARCHAR(24) not null
);

CREATE TABLE task_status (
    task_status_id    serial primary key,
    task_status_name    VARCHAR(24) not null
);

CREATE TABLE users (
    users_id       SERIAL PRIMARY KEY,
    username       VARCHAR(40) not null,
    password           VARCHAR(256) not null,
    email          VARCHAR(128) not null,
    email_verified boolean not null default false,
	roles_id	   serial not null,
    account_status_id       serial not null,
    created_on     TIMESTAMP  NOT NULL,  
    CONSTRAINT fk_roles
        FOREIGN KEY(roles_id) 
        REFERENCES roles(roles_id),
    CONSTRAINT fk_account_status
        FOREIGN KEY(account_status_id) 
        REFERENCES account_status(account_status_id)
);

CREATE TABLE profiles (
    profile_id       INT GENERATED ALWAYS AS IDENTITY,
	users_id	   serial not null,
    bio       VARCHAR(40) not null,
    goals           VARCHAR(256) not null,
    phone          VARCHAR(40) not null,
    phone_verified boolean not null default false,
	availabiltiy       VARCHAR(5000),   
    PRIMARY KEY(profile_id),
    CONSTRAINT fk_users
        FOREIGN KEY(users_id) 
        REFERENCES users(users_id)
);

CREATE TABLE tasks (
    task_id       INT GENERATED ALWAYS AS IDENTITY,
	assigned_by	   serial not null,
    assigned_to	   serial not null,
    task_status       serial,
    date_assigned           TIMESTAMP not null,
    date_completed           TIMESTAMP,
    target_date         TIMESTAMP,
    task_title boolean not null,
	task_body       VARCHAR(5000),   
    PRIMARY KEY(task_id),
    CONSTRAINT fk_users_assigned_by
        FOREIGN KEY(assigned_by) 
        REFERENCES users(users_id),
    CONSTRAINT fk_users_assigned_to
        FOREIGN KEY(assigned_to) 
        REFERENCES users(users_id),
    CONSTRAINT fk_task_status
        FOREIGN KEY(task_status) 
        REFERENCES task_status(task_status_id)
);

INSERT INTO task_status (task_status_name) VALUES ('Not Started');
INSERT INTO task_status (task_status_name) VALUES ('In Progress');
INSERT INTO task_status (task_status_name) VALUES ('Completed');
INSERT INTO task_status (task_status_name) VALUES ('Abandoned');
INSERT INTO task_status (task_status_name) VALUES ('Postponed');

INSERT INTO account_status (account_status_name) VALUES ('Pending');
INSERT INTO account_status (account_status_name) VALUES ('Approved');
INSERT INTO account_status (account_status_name) VALUES ('Revoked');

INSERT INTO roles (role_name) VALUES ('Admin');
INSERT INTO roles (role_name) VALUES ('User');
