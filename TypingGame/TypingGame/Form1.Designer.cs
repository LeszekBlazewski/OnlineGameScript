namespace TypingGame
{
    partial class FormMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.listBoxLetters = new System.Windows.Forms.ListBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.statusStripScore = new System.Windows.Forms.StatusStrip();
            this.correctLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.missedLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.totalLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.accuracyLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.DifficultyLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.DifficultyProgressBar = new System.Windows.Forms.ToolStripProgressBar();
            this.statusStripScore.SuspendLayout();
            this.SuspendLayout();
            // 
            // listBoxLetters
            // 
            this.listBoxLetters.Dock = System.Windows.Forms.DockStyle.Fill;
            this.listBoxLetters.Font = new System.Drawing.Font("Microsoft Sans Serif", 72F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.listBoxLetters.FormattingEnabled = true;
            this.listBoxLetters.ItemHeight = 108;
            this.listBoxLetters.Location = new System.Drawing.Point(0, 0);
            this.listBoxLetters.MultiColumn = true;
            this.listBoxLetters.Name = "listBoxLetters";
            this.listBoxLetters.Size = new System.Drawing.Size(856, 131);
            this.listBoxLetters.TabIndex = 0;
            // 
            // timer1
            // 
            this.timer1.Interval = 800;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // statusStripScore
            // 
            this.statusStripScore.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.correctLabel,
            this.missedLabel,
            this.totalLabel,
            this.accuracyLabel,
            this.DifficultyLabel,
            this.DifficultyProgressBar});
            this.statusStripScore.Location = new System.Drawing.Point(0, 109);
            this.statusStripScore.Name = "statusStripScore";
            this.statusStripScore.Size = new System.Drawing.Size(856, 22);
            this.statusStripScore.SizingGrip = false;
            this.statusStripScore.TabIndex = 1;
            this.statusStripScore.Text = "statusStrip1";
            // 
            // correctLabel
            // 
            this.correctLabel.Name = "correctLabel";
            this.correctLabel.Size = new System.Drawing.Size(55, 17);
            this.correctLabel.Text = "Correct:0";
            // 
            // missedLabel
            // 
            this.missedLabel.Name = "missedLabel";
            this.missedLabel.Size = new System.Drawing.Size(53, 17);
            this.missedLabel.Text = "Missed:0";
            // 
            // totalLabel
            // 
            this.totalLabel.Name = "totalLabel";
            this.totalLabel.Size = new System.Drawing.Size(42, 17);
            this.totalLabel.Text = "Total:0";
            // 
            // accuracyLabel
            // 
            this.accuracyLabel.Name = "accuracyLabel";
            this.accuracyLabel.Size = new System.Drawing.Size(75, 17);
            this.accuracyLabel.Text = "Accuracy:0%";
            // 
            // DifficultyLabel
            // 
            this.DifficultyLabel.Name = "DifficultyLabel";
            this.DifficultyLabel.Size = new System.Drawing.Size(514, 17);
            this.DifficultyLabel.Spring = true;
            this.DifficultyLabel.Text = "Difficulty";
            this.DifficultyLabel.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // DifficultyProgressBar
            // 
            this.DifficultyProgressBar.Maximum = 701;
            this.DifficultyProgressBar.Name = "DifficultyProgressBar";
            this.DifficultyProgressBar.Size = new System.Drawing.Size(100, 16);
            // 
            // FormMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(856, 131);
            this.Controls.Add(this.statusStripScore);
            this.Controls.Add(this.listBoxLetters);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D;
            this.KeyPreview = true;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "FormMain";
            this.Text = "Hit the keys !";
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.FormMain_KeyDown);
            this.statusStripScore.ResumeLayout(false);
            this.statusStripScore.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox listBoxLetters;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.StatusStrip statusStripScore;
        private System.Windows.Forms.ToolStripStatusLabel correctLabel;
        private System.Windows.Forms.ToolStripStatusLabel missedLabel;
        private System.Windows.Forms.ToolStripStatusLabel totalLabel;
        private System.Windows.Forms.ToolStripStatusLabel accuracyLabel;
        private System.Windows.Forms.ToolStripStatusLabel DifficultyLabel;
        private System.Windows.Forms.ToolStripProgressBar DifficultyProgressBar;
    }
}

