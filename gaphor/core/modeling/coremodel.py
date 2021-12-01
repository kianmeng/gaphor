# This file is generated by coder.py. DO NOT EDIT!
# isort: skip_file
# flake8: noqa F401,F811
# fmt: off

from __future__ import annotations

from typing import Callable

from gaphor.core.modeling.properties import (
    association,
    attribute as _attribute,
    derived,
    derivedunion,
    enumeration as _enumeration,
    redefine,
    relation_many,
    relation_one,
)


# 1: override Element
from gaphor.core.modeling.element import Element



# 4: override Diagram
from gaphor.core.modeling.diagram import Diagram



# 7: override Presentation
from gaphor.core.modeling.presentation import Presentation



class Comment(Element):
    annotatedElement: relation_many[Element]
    body: _attribute[str] = _attribute("body", str)


# 13: override StyleSheet
from gaphor.core.modeling.stylesheet import StyleSheet




Element.presentation = association("presentation", Presentation, opposite="subject")
Element.comment = association("comment", Comment, opposite="annotatedElement")
Element.ownedElement = derivedunion("ownedElement", Element)
Element.owner = derivedunion("owner", Element, upper=1)
Element.ownedDiagram = association("ownedDiagram", Diagram, composite=True, opposite="element")
Element.ownedElement.add(Element.ownedDiagram)  # type: ignore[attr-defined]
# 10: override Diagram.qualifiedName: property[list[str]]
# defined in gaphor.core.modeling.diagram

Diagram.ownedPresentation = association("ownedPresentation", Presentation, composite=True, opposite="diagram")
Diagram.element = association("element", Element, upper=1, opposite="ownedDiagram")
Element.ownedElement.add(Diagram.ownedPresentation)  # type: ignore[attr-defined]
Element.owner.add(Diagram.element)  # type: ignore[attr-defined]
Presentation.parent = association("parent", Presentation, upper=1, opposite="children")
Presentation.children = association("children", Presentation, composite=True, opposite="parent")
Presentation.subject = association("subject", Element, upper=1, opposite="presentation")
Presentation.diagram = association("diagram", Diagram, upper=1, opposite="ownedPresentation")
Element.owner.add(Presentation.diagram)  # type: ignore[attr-defined]
Comment.annotatedElement = association("annotatedElement", Element, opposite="comment")
