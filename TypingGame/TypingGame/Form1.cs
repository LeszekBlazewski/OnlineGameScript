using System;
using System.Windows.Forms;

namespace TypingGame
{
    public partial class FormMain : Form
    {
        Random random = new Random();
        Stats stats = new Stats();
        public FormMain()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
           
            ///Ad a random key to the ListBox
            listBoxLetters.Items.Add((Keys)random.Next(65, 90));
            if(listBoxLetters.Items.Count > 7)
            {
                listBoxLetters.Items.Clear();
                listBoxLetters.Items.Add("Game over !");
                timer1.Stop();
            }
        }
        /// <summary>
        /// Handels the events after a button is being pressed.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void FormMain_KeyDown(object sender, KeyEventArgs e)
        {
            // If the user pressed a key that's in the Listbox, remove it
            // and then make the game a little bit faster

            if(listBoxLetters.Items.Contains(e.KeyCode))
            {
                listBoxLetters.Items.Remove(e.KeyCode);
                listBoxLetters.Refresh();
                if (timer1.Interval > 400)
                    timer1.Interval -= 10;
                if (timer1.Interval > 250)
                    timer1.Interval -= 7;
                if (timer1.Interval > 100)
                    timer1.Interval -= 2;
                DifficultyProgressBar.Value = 800 - timer1.Interval;

                // The user pressed correct key so update the Stats object by calling the stats method Update() with arq true
                stats.Uptade(true);
            }

            else
            {
                // The user pressed a incorrect key so uptade the Stats object by calling the stats method Update with arq false
                stats.Uptade(false);
            }

            //Update the labels on the StatusStrip
            correctLabel.Text = "Correct: " + stats.correct;
            missedLabel.Text = "Missed: " + stats.missed;
            totalLabel.Text = "Total: " + stats.total;
            accuracyLabel.Text = "Accuracy: " + stats.accuracy + "%";

        }
    }
}
