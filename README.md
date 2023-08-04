# shepherd
Initialize multiple tmux pane sessions (sheep), all controlled by one shepherd.

## dependencies
1. tmuxp

## usage
1. Start the `shepherd` python shell
  ```
  tmuxp load shepherd.yaml
  ```
1. Birth a sheep
   ```
   >>> lamb(['echo "Baahh, I\'m Dolly!"'])
   ```
1. Heck, birth some more
   ```
   >>> for i in range(4):
   ...     lamb([f'echo "I am Dolly-{i}"'])
   ```
1. Start herding!
   ```
   >>> herd()
   ```   
   
