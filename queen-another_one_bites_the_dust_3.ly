#(define (tie::tab-clear-tied-fret-numbers grob)
   (let* ((tied-fret-nr (ly:spanner-bound grob RIGHT)))
      (ly:grob-set-property! tied-fret-nr 'transparent #t)))

\version "2.10.5"
\paper {
   indent = #0
   printallheaders = ##t
   print-all-headers = ##t
   ragged-right = ##f
   ragged-bottom = ##t
}
\layout {
   \context { \Score
      \override MetronomeMark #'padding = #'5
   }
   \context { \Staff
      \override TimeSignature #'style = #'numbered
      \override StringNumber #'transparent = ##t
   }
   \context { \TabStaff
      \override TimeSignature #'style = #'numbered
      \override Stem #'transparent = ##t
      \override Beam #'transparent = ##t
      \override Tie  #'after-line-breaking = #tie::tab-clear-tied-fret-numbers
   }
   \context { \TabVoice
      \override Tie #'stencil = ##f
   }
   \context { \StaffGroup
      \consists "Instrument_name_engraver"
   }
}
deadNote = #(define-music-function (parser location note) (ly:music?)
   (set! (ly:music-property note 'tweaks)
      (acons 'stencil ly:note-head::print
         (acons 'glyph-name "2cross"
            (acons 'style 'special
               (ly:music-property note 'tweaks)))))
   note)

palmMute = #(define-music-function (parser location note) (ly:music?)
   (set! (ly:music-property note 'tweaks)
      (acons 'style 'do (ly:music-property note 'tweaks)))
   note)

TrackAVoiceAMusic = #(define-music-function (parser location inTab) (boolean?)
#{
   \tempo 4=60
   \clef #(if $inTab "tab" "bass_8")
   \key c \major
   \time 4/4
   \oneVoice
   r2 r4 r8 <a,,\4>16 <g,,\4>16 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r4 r8 <a,,\4>16 <g,,\4>16 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>16 <g,\2>16 r8 <g,,\4>8 r8 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>8 r8 <g,,\4>8 r8 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>16 <g,\2>16 r8 <g,,\4>8 r8 
   <a,,\4>8 <a,,\4>8 r16 <a,,\4>16 r16 <ais,,\4>16 <b,,\4>8 r8 <b,,\4>16 <g,,\4>8. 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <fis,,\4>8 r8 r16 <b,,\4>8 <ais,,\4>16 <a,,\4>8 <a,,\4>8 <a,,\4>8 r8 
   <fis,,\4>8 r8 r4 r4 <g,,\4>4 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>16 <g,\2>16 r8 <g,,\4>8 r8 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>8 r8 <g,,\4>8 r8 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>16 <g,\2>16 r8 <g,,\4>8 r8 
   <a,,\4>8 <a,,\4>8 r16 <a,,\4>16 r16 <ais,,\4>16 <b,,\4>8 r8 r4 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <fis,,\4>8 r8 r16 <b,,\4>8 <ais,,\4>16 <a,,\4>8 <a,,\4>8 <a,,\4>8 r8 
   <fis,,\4>8 r8 r4 r4 <\bendAfter #+6 g,,\4>4 
   <e,,\4>8 r8 r4 r2 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r1 
   r2 r4 r8 <a,,\4>16 <g,,\4>16 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r4 r8 <a,,\4>16 <g,,\4>16 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>16 <g,\2>16 r8 <g,,\4>8 r8 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>8 r8 <g,,\4>8 r8 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>16 <g,\2>16 r8 <g,,\4>8 r8 
   <a,,\4>8 <a,,\4>8 r16 <a,,\4>16 r16 <ais,,\4>16 <b,,\4>8 r8 <b,,\4>16 <g,,\4>8. 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <fis,,\4>8 r8 r16 <b,,\4>16 r16 <ais,,\4>16 <a,,\4>8 <a,,\4>8 <a,,\4>8 r8 
   <fis,,\4>8 r8 r4 r4 <g,,\4>4 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r4 r8 <a,,\4>16 <g,,\4>16 
   <e,,\4>8 r8 <e,,\4>8 r8 <e,,\4>8 r8 r8. <e,,\4>16 
   <e,,\4>8 <e,,\4>8 <g,,\4>8 <e,,\4>16 <a,,\4>16 r2 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>16 <g,\2>16 r8 <g,,\4>8 r8 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>8 r8 <g,,\4>8 r8 
   <c,\3>8 <c,\3>8 r16 <c,\3>16 r16 <cis,\3>16 <d,\3>16 <g,\2>16 r8 <g,,\4>8 r8 
   <a,,\4>8 <a,,\4>8 r16 <a,,\4>16 r16 <ais,,\4>16 <b,,\4>8 r8 <b,,\4>16 <g,,\4>8. 
   <e,,\4>8 r8 r4 r2 
   \bar "|."
   \pageBreak
#})
TrackAVoiceBMusic = #(define-music-function (parser location inTab) (boolean?)
#{
#})
TrackALyrics = \lyricmode {
   \set ignoreMelismata = ##t
   
   \unset ignoreMelismata
}
TrackAStaff = \new Staff <<
   \context Voice = "TrackAVoiceAMusic" {
      \TrackAVoiceAMusic ##f
   }
   \context Voice = "TrackAVoiceBMusic" {
      \TrackAVoiceBMusic ##f
   }
>>
TrackATabStaff = \new TabStaff \with { stringTunings = #'( -17 -22 -27 -32 ) } <<
   \context TabVoice = "TrackAVoiceAMusic" {
      \removeWithTag #'chords
      \removeWithTag #'texts
      \TrackAVoiceAMusic ##t
   }
   \context TabVoice = "TrackAVoiceBMusic" {
      \removeWithTag #'chords
      \removeWithTag #'texts
      \TrackAVoiceBMusic ##t
   }
>>
TrackAStaffGroup = \new StaffGroup <<
   \TrackAStaff
   \TrackATabStaff
>>
\score {
   \TrackAStaffGroup
   \header {
      title = "Another One Bites The Dust" 
      composer = "" 
      instrument = "Deacon" 
   }
}
