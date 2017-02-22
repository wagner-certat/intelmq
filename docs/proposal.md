# Summary

There are two (new) concepts:
* Automatic starting; On boot and with `intelmqctl start`
* Scheduling via crontab

# Configuration

* `enabled` is replaced by `autostart`, which is a better name.
* new parameter `scheduled_time` with a time specification in crontab syntax. Default for oneshots is "0 0 * * *" i.e. midnight
* `run_mode` can be "stream" or "oneshot" (or other names, TBD). Default is "stream"

# Commands

## start

```bash
> intelmqctl start
```
All bots with the flag `autostart` set to true, will be started now (no changes here). Independent of the run mode.

```bash
> intelmqctl start [bot-id]
```
The bot with ID bot-id will be started now, independent of the run mode (no changes here).

TODO: What happens if the run_mode of a bot changed?
## stop
Stopp all running bots, independent of the run mode(s) (no changes here).

## restart
Stop and start (no changes here).

TODO: also the scheduled ones?

## reload
No changes here: Send SIGHUP to all running bots.

TODO: What happens if the run_mode of a bot changed?

Rewrite the crontab file to update the scheduled times for all bots with run_mode scheduled.

## status
Can have status running / stopped / scheduled.

## autostart / noautostart
Set the autostart flag to True/False.

Enable the bot on boot with the process manager. (intelmq: write at most one entry of `@reboot intelmqctl start` to crontab, systemd: `systemctl enable bot-name@bot-id`)

## schedule / unschedule

```bash
> intelmqctl schedule
```
Update the crontab file for all bots with run_mode = scheduled with time from runtime.

```bash
> intelmqctl schedule bot-id
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

# Reasoning

Autostart can be true for scheduled bots. This implies that they will be additionally be started on boot and on `intelmqctl start`.

Can be discussed if this is unwanted or considered harmful.

# crontab

The crontab entry which will be written looks like this:

```crontab
<timespec>  intelmqctl start bot-id # IntelMQ bot bot-id
```

The comment is the identifier. Used for parsing the file.

## autostart on boot

If the PID process management is used, this additional crontab entry exists:
```cron
@reboot intelmqctl start
```

This will "simulate" the same behavior as enabled services.