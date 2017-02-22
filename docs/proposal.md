# Summary

There are two (new) concepts:
* Automatic starting; On boot and with `intelmqctl start`
* Scheduling via crontab

# Configuration

* `enabled` is replaced by `autostart`, which is a better name.
* new parameter `scheduled_time` with a time specification in crontab syntax. Default for scheduled is "0 0 * * *" i.e. midnight
* `run_mode` can be "continous" or "scheduled". Default is "continous"

# Commands

## start

```bash
> intelmqctl start
```
All bots with the flag `autostart` set to true, will be started now. 

```bash
> intelmqctl start [bot-id]
```
The bot with ID bot-id will be started now.

TODO: What happens if the run_mode of a bot changed?

## stop
Stop all currently running bots via SIGTERM, independent of the run mode(s).

## restart
Stop and start all currently running bots (i.e. do not extra start the "scheduled" ones

## reload
No changes here: Send SIGHUP to all running bots.

TODO: What happens if the run_mode of a bot changed?

Rewrite the crontab file to update the scheduled times for all bots with run_mode scheduled.

## status
Can have status running / stopped / scheduled.

## autostart / noautostart
Set the autostart flag to True/False.

Enable the bot on boot with the process manager. (intelmq: write at most one entry of `@reboot intelmqctl start` to crontab, systemd: `systemctl enable bot-name@bot-id`)

Only applies to bots with run mode = continous.

## schedule / unschedule

```bash
> intelmqctl schedule
```
Update the crontab file for all bots with run_mode = scheduled with time from runtime.

```bash
> intelmqctl schedule bot-id [timespec]
```
Update the crontab entry of the given bot (with the given timespec), and/or uncomment if existing.
Ensure that run_mode for the bot is scheduled and a valid time is given.

```bash
> intelmqctl unschedule
```
Comment (Delete?) the crontab entry of all bots.

```bash
> intelmqctl unschedule bot-id
```
Comment (Delete?) the crontab entry of the given bot.

## check
It additionally checks for consistency of
* currently running bots and configured bots
* bots configured in crontab and runtime configuration

# Explanation: crontab

The crontab entry which will be written looks like this:

```perl
<timespec>  intelmqctl start bot-id # IntelMQ bot bot-id
```

The comment is the identifier. Used for parsing the file.
